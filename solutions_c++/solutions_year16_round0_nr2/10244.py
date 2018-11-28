#include<bits/stdc++.h>
#define ll long long
using namespace std;

void func() {
	string s;
	cin>>s;
	ll l = s.length();
	ll ctr=0;
	for(ll i=0;i<l-1;i++) {
		if(s[i]!=s[i+1]) ctr++;
	}
	if(s[l-1]=='-') ctr++;
	cout<<" "<<ctr;
}

int main() {
	ll n,i;
	cin>>n;
	for(i=1;i<=n;i++) {
		cout<<"Case #"<<i<<":";
		func();
		cout<<endl;
	}
}
