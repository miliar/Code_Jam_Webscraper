#include<iostream>
#include<cstdio>
using namespace std;
int n;
typedef long long ll;
ll p;
bool poss2(ll p,ll i,int r){
	if(i==0 || p==0)return 1;
	if(i==(1ll<<r)-1 && p>0)return 0;
	int r2=r-1;
	if(p&1ll<<r2){
		return poss2(p^1ll<<r2,i+1>>1,r2);
	}else{
		return i+1<(1ll<<r);
	}
}
ll solve2(){
	ll L=0,R=1ll<<n;
	for(;L+1<R;){
		ll M = (L+R)/2;
		if(poss2(p,M,n))L=M;
		else R = M;
	}
	return L;
}
bool sure1(ll p,ll i,int r){
	if(i==0)return 1;
	int r2=r-1;
	if(p&1ll<<r2){
		return i==0;
	}else{
		return sure1(p,(1ll<<r2)-1-((1ll<<r)-i)/2,r2);
	}
}
ll solve1(){
	ll L=0,R=1ll<<n;
	for(;L+1<R;){
		ll M = (L+R)/2;
		if(sure1(p,M,n))L=M;
		else R = M;
	}
	return L;
}
int main(){
	int ts=1,Ts;
	for(cin >>Ts;Ts--;++ts){
		cin >> n >> p;
		p = (1ll<<n) - p;
		cout << "Case #"<<ts << ": " <<
		solve1() <<" " << solve2() << endl;
	}
}
