#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ size()
#define ST begin()
#define ED end()
#define CLR clear()
#define ZERO(x) memset((x),0,sizeof(x))
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
const double EPS = 1e-8;

const int MAX_N = 1111;
int D,T,P[MAX_N];
int ans;

int getMax(){
	for(int i=1000;i>=1;i--) if(P[i]) return i;
	return -1;
}

void dfs(int NowTime){
	int Max = getMax();
	ans = min(Max+NowTime,ans);
	if(Max==1) return;
	for(int i=Max-1;i>=Max>>1;i--){
		int tmp = P[Max];
		P[i]+=tmp;
		P[Max-i]+=tmp;
		P[Max] = 0;
		dfs(NowTime+tmp);
		P[Max] = tmp;
		P[i]-=tmp;
		P[Max-i]-=tmp;
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int cases = 1; cases <= T; cases++){
		scanf("%d",&D);
		ZERO(P);
		ans = 0;
		for(int i=0;i<D;i++){
			int t;
			scanf("%d",&t);
			P[t]++;
			ans = max(ans,t);
		}
		dfs(0);
		printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}