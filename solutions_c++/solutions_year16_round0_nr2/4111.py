#include <bits/stdc++.h>
#define ll unsigned long long
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	for(int j = 1; j<=t; j++){
		string s;
		cin>>s;
		ll c = 0, l = s.length();
		for(int i = 1; i<l; i++){
			if(s[i]!=s[i-1]){
				c++;
			}
		}
		if(s[l-1]=='+'){
			cout<<"Case #"<<j<<": "<<c<<endl;
		}
		else{
			cout<<"Case #"<<j<<": "<<c+1<<endl;
		}
	}
	return 0;
}
