#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#define fr(i,a,b) for(int i=a;i<b;i++)
#define rep(i,b) fr(i,0,b)
using namespace std;
typedef long long ll;
#define N 10000000

bool pali(ll a){
	ll aa = a, fa=1LL;
	while(aa) aa/=10LL, fa*=10LL;
	while(a){
		fa/=10LL;
		if(a/fa != a%10) return false;
		a -= (a/fa)*fa;
		a/=10LL;
		fa/=10LL;
	}
	return true;
}
ll val[1000000];
int main(){	
	int rsp=0;
	for(ll i=1;i<10000010;i++){
		if(pali(i) && pali(i*i)) val[rsp++] = i*i;
	}
	int cas;
	cin >> cas;
	rep(u,cas){
		ll a, b;
		cin >> a >> b;
		int pa = lower_bound(val,val+rsp,a)-val;
		int pb = upper_bound(val,val+rsp,b)-val;
		printf("Case #%d: %d\n",u+1,pb-pa);
	}
	
	return 0;
}

