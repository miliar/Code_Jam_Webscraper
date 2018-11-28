#include<iostream>
#include<string.h>
#include <fstream>
std::ifstream infile("thefile.in");
std::ofstream offile("out.txt");
using namespace std;
int compute(string s){
	char prev=s[0];
	
	int c=1;
	for(int i=0;i<s.length();i++){
		if(s[i]!=prev){
			c++;
			
			prev=s[i];
		}
		
	}
	if(prev=='+'){
		return c-1;
	}else return c;
	
}
int main(){
	int t;
	string s;
	
	infile>>t;
	for(int i=0;i<t;i++){
	    infile>>s;
		offile<<"Case #"<<i+1<<": "<<compute(s)<<endl;
	}
	
	
	
	
	
	
	
	
	return 0;
}
