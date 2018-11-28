#include<iostream>
#include<fstream>
#include<string>
using namespace std;

ifstream input("B-large.in",ios::in);
ofstream output("Revenge of the Pancakes_output.txt",ios::out);

long long t,l,k,pos,neg,i;
string s;

int main(){
	input>>t;
	for(k=1;k<=t;++k){
		input>>s;
		l=s.length();
		pos=neg=0;
		for(i=0;i<l;++i){
			if(s[i]=='+') neg=pos+1;
			else pos=neg+1;
		}
		output<<"Case #"<<k<<": "<<pos<<endl;
	}
	return 0;
}
