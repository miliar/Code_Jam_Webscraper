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
int n;
int ary[maxn + geps];

void Init(){
	scanf("%d",&n);
	repk(i,0,n){
		scanf("%d",ary+i);
	}
}

void solve(){
	int ans1 = 0;
	repk(i,1,n){
		if(ary[i-1] - ary[i] > 0)
			ans1 += ary[i-1] - ary[i];
	}
	int v = 0;
	repk(i,1,n){
		v = max(v,ary[i-1] - ary[i]);
	}
	int ans2 = 0;
	repk(i,1,n){
		ans2 += min(v, ary[i-1]);
	}
	printf("%d %d\n",ans1, ans2);
}

int main(){

	int Test;
	scanf("%d",&Test);
	for(int t = 0; t < Test; ++t){
		Init();
		printf("Case #%d: ", t+1);
		solve();
	}
	
	return 0;
}
