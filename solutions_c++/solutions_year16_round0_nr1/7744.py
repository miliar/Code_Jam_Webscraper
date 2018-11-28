#include<bits/stdc++.h>
#define ll long long
using namespace std;

void func() {
	ll a;
	cin>>a;
	if(a==0) {
		cout<<" INSOMNIA";
		return;
	}
	ll d=a;
	bool bl[10]={false};
	int ct=0;
	while(ct!=10) {
		ll b=d;
		while(b>0) {
			ll c=b%10;
			b = b/10;
			bl[c]=true;
		}
		while(bl[ct]==true && ct!=10) {
			ct++;
		}
		d = d+a;
	}
	d=d-a;
	cout<<" "<<d;
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
