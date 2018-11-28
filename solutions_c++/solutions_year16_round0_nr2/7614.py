#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	int cs=1;
	cin.ignore(10000,'\n');
	while(t--){
		string s;
		getline(cin,s);
		int ct=1;
		char c = s[0];
		for(int i =0; i<s.size();i++){
			if(s[i] != c){
				ct++;
			}
			c = s[i];
		}
		if(c == '+') ct--;
		cout<<"Case #"<<cs++<<": "<<ct<<endl;
	}
	return 0;
}