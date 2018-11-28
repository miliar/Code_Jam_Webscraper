#include<bits/stdc++.h>

using namespace std;

int generateAll(string s, map<string, int>& hash){
	if(s.length() > 15)
		return 0;
	if(s[0] == '-'){
		hash['-'+s] = hash[s];
		hash['+'+s] = hash[s] + 1;
	}
	else{
   		hash['-'+s] = hash[s] + 1;
		hash['+'+s] = hash[s] ;
	}
	generateAll('-'+s, hash);
	generateAll('+'+s,hash);
	return 0;
}

int main() {
	int tCase;
	cin>>tCase;
	map<string,int> hash;
	hash["-"] = 1;
	hash["+"] = 0;
	generateAll ("-",hash);
	generateAll("+",hash);

	for (int i=1; i<=tCase; ++i) {
	      string s;
	      cin>>s;
	      if( s.length() < 16)
		cout<<"Case #"<<i<<": "<<hash[s]<<endl;
	      else {
	      	long long ans = 0;
	      	while(s.length() > 15){
	      		if(s[0] != s[1]){
	      		     ++ans;
	      		}
	      		s.erase(s.begin());
	      	}
	      	cout<<"Case #"<<i<<": "<<hash[s]+ans<<endl;
	      }
	}
	return 0;
}