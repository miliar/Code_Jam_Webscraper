/*
 * totoroXD
 *
 */
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <limits>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;
typedef long long LL;
const int INF = 1011110000, MOD=1000000000;
const int dx[]={1,0,-1,0}, dy[]={0,1,0,-1};
const double EPS = 1e-6;
typedef long long LL;
int kase=1;
LL p, q;
LL gcd(LL a, LL b){
	if(a>b)swap(a,b);
	if(a==0)return b;
	return gcd(a, b%a);
}
int nBits(LL num){
	int res=0;
	while(0<num){
		if(num%2==1)res++;
		num/=2;
	}
	return res;
}
bool checkPow(LL num){
	while(1<num){
		if(num%2==1)return 0;
		num/=2;
	}
	return 1;
}
int ans(LL p, LL q){
	int k=0;
	while(1<q){
		if(p%2==1)k=0;
		q/=2;
		p/=2;
		k++;
	}
	return k;
}
bool input(){
	scanf("%lld/%lld",&p,&q);
	return 1;
}
void solve(){
	printf("Case #%d: ",kase++);
	LL d=gcd(p,q);
	p/=d;
	q/=d;
	if(!checkPow(q)){
		printf("Impossible\n");
		return;
	}
	printf("%d\n",ans(p, q));
}
void pre(){
}
int main(){
	pre();
    int zz=1;
    cin>>zz;
    while(zz--){
    	input();
    	solve();
    }
    return 0;
}

/*

5
1/2
3/4
1/4
2/23
123/31488


*/

