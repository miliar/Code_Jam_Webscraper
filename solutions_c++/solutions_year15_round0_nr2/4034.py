#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <bitset>
#include <algorithm>

using namespace std;

#define LL long long
#define pii pair<int,int>

const int INF = 0x3f3f3f3f;

int h[11];

void dfs(int mx , int ad , int& ans){
	for(int i = 1; i <= mx / 2; ++i){
		int x[11] , cur , tp; for(int z = 0; z <= 10; ++z) x[z] = h[z];
		h[i] += h[mx]; h[mx - i] += h[mx]; tp = ad + h[mx]; h[mx] = 0;
		for(int z = mx-1; z >= 1; --z)
			if(h[z] > 0) { cur = z; break;	 }
		ans = min(ans,tp+cur);
		dfs(cur,ad+tp,ans);
		for(int z = 0; z <= 10; ++z) h[z] = x[z];
	}
}

int main(){
	freopen("B-small-attempt5.in","r",stdin);
	freopen("B5.out","w",stdout);
	int T; scanf("%d",&T);
	for(int kase = 1; kase <= T; ++kase){
		memset(h,0,sizeof(h));
		int D, p , mx = 0;
		scanf("%d",&D);
		for(int i = 0; i < D; ++i){
			scanf("%d",&p);
			++h[p];
			mx = max(mx,p);
		}
		int ans = mx , ad = 0;
		dfs(mx,ad,ans);
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
