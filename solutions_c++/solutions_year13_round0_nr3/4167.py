#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;
#define ll long long
#define maxn 10000007
int T;
int cc=0;
ll a,b;
ll l,r;
int tree[maxn];
int lowbit(int x){
	return x&-x;
}
void add(int x){
	while(x<maxn){
		tree[x]++;
		x+=lowbit(x);
	}
}
int sum(int x){
	int ret=0;
	while(x>0){
		ret+=tree[x];
		x-=lowbit(x);
	}
	return ret;
}
bool pal(ll num){
	int t=num;
	int cp=0;
	while(num){
		cp*=10;
		cp+=num%10;
		num/=10;
	}
	return t==cp;
}
void check(int curr){
	if(!pal((ll)curr)){
		return;
	}
	ll t=curr;
	t*=curr;
	if(pal(t)){
	//	if(curr<=1000){
	//	cout<<curr<<endl;
	//	}
		add(curr);
	}
}
int main(){
#ifdef LOCAL
	freopen("c.txt","r",stdin);
	freopen("c.out","w",stdout);
#endif
	cin>>T;
	for(int i=1;i<1e7+1;i++){
		check(i);
	}
	while(cc<T){
		cin>>a>>b;
		l=ceil(sqrt(a*1.0));
		r=floor(sqrt(b*1.0));
		//cout<<a<<" "<<b<<endl;
		//cout<<l<<" "<<r<<endl;
		//cout<<"check done"<<endl;
		cout<<"Case #"<<++cc<<": ";
		cout<<sum(r)-sum(l-1)<<endl;
	}
}
