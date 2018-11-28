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
char input[maxn + geps];
int sum[maxn + geps];
int n;
void Init(){
	scanf("%d%s",&n,input);
	sum[0] = input[0] - '0';
	rep(i,1,n) sum[i] = sum[i-1] + input[i] - '0';
}

void solve(){
	int ans = 0;
	rep(i,1,n) if(input[i] != '0') ans = max(ans, i - sum[i-1]);
	//repk(i,0,n) printf("%d %d\n",sum[i], i - sum[i-1]);
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
