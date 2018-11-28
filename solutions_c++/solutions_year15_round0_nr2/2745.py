#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <cstring>
using namespace std;
#define rep(i,a,b) for(int i = (a);i<=(b);i++)
#define repk(i,a,b) rep(i,(a),(b)-1)
#define rrep(i,a,b) for(int i = (b);i>=(a);i--)
#define rrepk(i,a,b) rrep(i,(a),(b)-1)
const int inf = 0x3fffffff,dinf = 0x7fffffff,geps = 10;
typedef long long LL;

const int maxn = 1000;
int ary[maxn + geps];
int n;

void Init(){
	scanf("%d",&n);
	repk(i,0,n) scanf("%d",ary+i);
}

int updiv(int x,int y){
	return (x + y - 1) / y;
}

void solve(){
	int tmax = 0, ans = inf;
	repk(i,0,n) tmax = max(ary[i], tmax);
	rep(h,1,tmax){
		int cnt = 0;
		repk(i,0,n) cnt += updiv(ary[i],h) - 1;
		ans = min(ans, cnt + h);
	}
	printf("%d\n",ans);
}

int main(){

	int T;
	scanf("%d",&T);
	repk(t,0,T){
		Init();
		printf("Case #%d: ",t+1);
		solve();
	}
	
	return 0;
}
