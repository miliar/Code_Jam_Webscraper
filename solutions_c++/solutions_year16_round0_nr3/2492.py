#include<bits/stdc++.h>
#define ll long long

using namespace std;

stack < char > stac;

bitset < 35 > b;

ll power(ll base,ll exp){
	ll ret=1;
	while(exp>0){
		if(exp & 1)ret=ret*base;
		base*=base;
		exp>>=1;
	}
	return ret;
}

bool check(ll a){
	ll i;
	for(i=2;i<a;i++){
		if(a%i==0)return false;
	}
	return true;
}

ll factorise(ll x){
	for(ll i=2;i<x;i++){
		if(x%i==0)return i;
	}
}

int main(){
	//pre();
	ll t,i,j,ans,n,k,temp;
	cin>>t;
	cout<<"Case #1:\n";
	cin>>n>>j;
	for(i=(1<<(n-1))+1;i<(1<<n) && j>0;i+=2){
		vector < ll > v;
		b=i;
		ll temp;
		for(k=2;k<=10;k++){
			temp=0;
			for(int l=0;l<n;l++){
				if(b[l])temp+=power(k,l);
			}
			if(check(temp))break;
			v.push_back(temp);
		}
		if(v.size()<9)continue;
		for(k=0;k<n;k++)cout<<b[k];
		cout<<' ';
		for(k=0;k<v.size();k++){
			cout<<factorise(v[k])<<' ';
		}
		cout<<"\n";
		j--;
	}
	return 0;
}
