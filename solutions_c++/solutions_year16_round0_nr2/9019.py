#include "bits/stdc++.h"
using namespace std;
int countS(string s){
	int c=0;
	for (int i = 0; i < s.length()-1; ++i){
		if(s[i]!=s[i+1])
			c++;
	}
	if(s[s.length()-1]=='-')
		c++;
	return c;
}
int main(int argc, char const *argv[])
{
	int t;
	string s;
	cin>>t;
	for (int i = 1; i <=t; ++i){
		cin>>s;
		cout<<"Case #"<<i<<": "<<countS(s)<<endl;
	}
	return 0;
}