#include <bits/stdc++.h>
using namespace std;
string s,t;
int main(){
	int test;
	cin>>test;
	for(int te=1;te<=test;te++){
		cin>>s;
		int n=s.size();
		t="";
		t+=s[0];
		for(int i=1;i<n;i++){
			if(t[t.size()-1]!=s[i])t+=s[i];
		}
//		cout<<t<<endl;
		int r=t.size()-1;
		if(t[r]=='-')r++;
		cout<<"Case #"<<te<<": "<<r<<endl;
	}		
	return 0;
}
