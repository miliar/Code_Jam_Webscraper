#include<iostream>
#include<stdio.h>
#define fr(i,a,b) for(i=a;i<=b;i++)
typedef long long ll;
using namespace std;
ll ti,ca,n,p,i,a,b;
ll cnt(ll r){
	int cnt=0;
	while(r>1){
		cnt++;
		r/=2;
	}
	return cnt;
}
ll bestCase(ll r){
	ll i,tmp=cnt((1<<n)-r),res=0;
	fr(i,1,n-tmp)
		res=res*2+1;
	return res;
}
ll worseCase(ll r){
	ll i,tmp=cnt(r+1),res=0;
	fr(i,1,tmp)
		res=res*2+1;
	return res*(1<<(n-tmp));
}
ll find1(ll le,ll ri){
	if(le==ri)
		return le;
	if(worseCase((le+ri)/2+1)<=p)
		return find1((le+ri)/2+1,ri);
	else
		return find1(le,(le+ri)/2);
}
ll find2(ll le,ll ri){
	if(le==ri)
		return le;
	if(bestCase((le+ri)/2+1)<=p)
		return find2((le+ri)/2+1,ri);
	else
		return find2(le,(le+ri)/2);
}

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n>>p;
		p--;
		cout<<"Case #"<<ti<<": "<<find1(0,(1<<n)-1)<<" "<<find2(0,(1<<n)-1)<<endl;
	}
}