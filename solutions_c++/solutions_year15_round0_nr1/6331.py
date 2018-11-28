#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;

int inviteNum(vector<int> l,int sum, int i, int invite){
	if(i==l.size()) {return invite;}
	else{
	if(sum+invite<i+1) return inviteNum(l, sum+l[i+1], i+1, i+1-sum);
	else return inviteNum(l, sum+l[i+1], i+1, invite);
	}
}

int main(int argc, char** argv) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    ifstream cin;
    cin.open(argv[1],ifstream::in);
    vector<int> result;
    while(cin.good()&&!cin.eof()){
        string line;
        string word; 
	vector<int> vec;
        getline(cin, line);
        stringstream ss(line);
	bool f=true;
        while(ss>>word){
            if(!word.empty()){
                if(f) {f=false;}
                else{
		for(unsigned int j=0;j<word.size();j++){
			stringstream ss2;
			ss2<<word[j];
                	int d;
			ss2>>d;
			//cout<<d<<endl;
                	vec.push_back(d);
		}
			int i=inviteNum(vec,vec[0],0,0);
			result.push_back(i);
			//cout<<i<<endl;
		}
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


