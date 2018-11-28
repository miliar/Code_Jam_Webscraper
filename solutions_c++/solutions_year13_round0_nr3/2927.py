//#pragma comment(linker, "/STACK:134217728,134217728") /*128Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#include <algorithm>
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

/*--in common define-----*/
#define N  110
#define E  100010
#define ll long long
const ll PRIME =999983;
const ll MOD   =1000000007;
const ll MULTI =1000000007;
/*--end in common define-*/

/*--in common use--------*/
#define cube(x) ((x)*(x)*(x))
#define sq(x)     ((x)*(x))
#define all(x)     x.begin(),x.end()
#define lp(a,s,t)   int (a)=(s);(a)<(t);(a)++
#define lpe(a,s,t) int (a)=(s);(a)<=(t);(a)++
inline bool isodd(int x){return x&1;}
inline bool isodd(ll x) {return x&1;}
/*--end in common use----*/

bool check(ll n)
{
	int digit[20],pos=0;
	while(n){
		digit[pos++]=n%10;
		n/=10;
	}
	for(int i=0;i<pos;i++)
		if(digit[i]!=digit[pos-i-1]) return false;
	return true;
}

int main() {

	int re,Case=1;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&re);
	while(re--){
		ll x,y;
		scanf("%lld %lld",&x,&y);
		ll cnt=0;
		y=sqrt(1.0*y);
		x=sqrt(1.0*x)+0.999999;
		for(ll i=x;i<=y;i++)
			if(check(i) && check(i*i)) cnt++;
		printf("Case #%d: %lld\n",Case++,cnt);
	}
	return 0;
}