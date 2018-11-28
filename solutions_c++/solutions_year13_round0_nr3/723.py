#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<vector>
#define fr(i,a,b) for(i=a;i<=b;++i)
#define ll long long
using namespace std;
vector<ll> lst;
ll i,ca,ti,a,b;
bool palindrome(ll r){
	vector<int> tmp;
	while(r>0){
		tmp.push_back(r%10);
		r/=10;
	}
	int i,n=tmp.size();
	fr(i,0,n/2-1)
		if(tmp[i]!=tmp[n-1-i])
			return false;
	return true;
}
int main(){
	freopen("c2.in","r",stdin);
	freopen("c2.out","w",stdout);
	fr(i,1,10000000)
		if(palindrome(i)&&palindrome(i*i))
			lst.push_back(i*i);
	cin>>ca;
	fr(ti,1,ca){
		cin>>a>>b;
		cout<<"Case #"<<ti<<": "<<upper_bound(lst.begin(),lst.end(),b)-lower_bound(lst.begin(),lst.end(),a)<<endl;
	}
}