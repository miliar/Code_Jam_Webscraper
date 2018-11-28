#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;

bool omino(vector<int> l){
	if(l[0]>l[1]&&l[0]>l[2]) return true;
		//(Rich) Too big;
	else if(l[1]*l[2]%l[0]!=0) return true;
		//(Rich) Cant fit;
	else if(l[0]>6) return true;
		//(Rich) hole;
	else{
		int min=0;
		int max=0;
		int h=(l[0]+1)/2;
		//cout<<h<<endl;
		if(l[1]>l[2]) {min=l[2];max=l[1];}
		else {min=l[1];max=l[0];}
		if(h>min) return true; 
		//Too high;
		if(l[0]==4) return min<3;
		if(l[0]==5) return max==5&&min==3;
		if(l[0]==6) return min<4;
		if(l[0]==1) return false;
	}
	return false;
}

int main(int argc, char** argv) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    ifstream cin;
    cin.open(argv[1],ifstream::in);
    bool f=true;
    vector<string> result;
    while(cin.good()&&!cin.eof()){
   	vector<int> vec;
        string line;
        string word; 
        getline(cin, line);
        stringstream ss(line);
        while(ss>>word){
            if(!word.empty()){
                if(f) {f=false;}
                else{
                int d=atoi(word.c_str());
                vec.push_back(d);
                }
            }
	}
	if(vec.size()==3){
	bool r=omino(vec);
	if(r) {result.push_back("RICHARD");
		//cout<<"R"<<endl;
		}
	else {result.push_back("GABRIEL");
		//cout<<"G"<<endl;
		}
	}
   }
   ofstream out;
   out.open("out.txt",std::ofstream::out);
   if(out.is_open()){
   for(unsigned int j=0;j<result.size();j++)
   out<<"Case #"<<j+1<<": "<<result[j]<<endl;}
	out.close();
    return 0;
}


