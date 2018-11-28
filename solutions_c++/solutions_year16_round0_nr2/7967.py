#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <cstdio>
using namespace std;
int ok(string s){
	for(char c:s)
		if(c=='-')
			return 0;
	return 1;
}
int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int T= 1; T<=t; T++){
		string s; 
		cin>>s;
		while(s[s.length()-1]=='+'){
			s=s.substr(0,s.length()-1);
		}
		if(s.length()==0){
			cout<<"Case #"<<T<<": "<<0<<"\n";
			continue;
		}
		int n = s.length();
		int ans = 1;
		for(int i = 1; i<n;i++){
			if(s[i]!=s[i-1])
				ans++;
		}
		cout<<"Case #"<<T<<": "<<ans<<"\n";
	}
	return 0;
}