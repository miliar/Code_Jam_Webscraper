#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;
vector<int> result;
int main(int argc, char** argv) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    ifstream cin;
    cin.open(argv[1],ifstream::in);
    bool f=true;
    while(cin.good()&&!cin.eof()){
        string line;
        string word;
    	vector<int> vec; 
        getline(cin, line);
        stringstream ss(line);
	int s1=0;
	int s2=0;
	int rate=0;
        while(ss>>word){
            if(!word.empty()){
                if(f) {f=false;}
                else{
                	int d=atol(word.c_str());
                	vec.push_back(d);
                }
            }
        }
	if(vec.size()>1){
		for(int j=1;j<vec.size();j++){
			if(vec[j-1]>vec[j]){
				s1+=vec[j-1]-vec[j];
				int t=(vec[j-1]-vec[j]);
				if(t>rate) rate=t;	
			}
		}
		for(unsigned int j=0;j<vec.size()-1;j++){
			if(rate>vec[j]){
				s2+=vec[j];
			}
			else s2+=rate;
		}
		result.push_back(s1);
		result.push_back(s2);
	}
   }
   ofstream out;
   out.open("out.txt",std::ofstream::out);
   if(out.is_open()){
	for(unsigned int j=1;j<result.size();j+=2)
	out<<"Case #"<<(j+1)/2<<": "<<result[j-1]<<" "<<result[j]<<endl;}
	out.close();
    return 0;
}


