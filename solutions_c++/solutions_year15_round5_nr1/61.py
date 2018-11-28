#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

const int N = 1e6+1000;

int next[N], last[N], to[N], tot;
int low[N], high[N];
int cnt[N];

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc=1; cc<=TT; ++cc){
		tot = 0;
		memset(last, -1, sizeof(last));
		memset(cnt, 0, sizeof(cnt));
		int n, d;
		scanf("%d%d", &n, &d);
		{
			int s, a, c, r;
			scanf("%d%d%d%d", &s, &a, &c, &r);
			low[0] = max(0, s-d);
			high[0] = s;
			for(int i = 1; i < n; ++i){
				s = (1ll * s * a + c) % r;
				low[i] = max(0, s - d);
				high[i]  = s;
			}
		}
		{
			int m, a, c, r;
			scanf("%d%d%d%d", &m, &a, &c, &r);
			for(int i = 1; i < n; ++i){
				m = (1ll * m * a + c) % r;
				int fa = m % i;
				low[i] = max(low [i], low[fa]);
				high[i] = min(high[i], high[fa]);
			}
		}
		for(int i=0; i<n; ++i){
			if(low[i] <= high[i]){
				cnt[low[i]]++;
				cnt[high[i]+1] --;
			}
		}
		int ans = 0, now = 0;
		for(int i=0; i<N; ++i){
			now += cnt[i];
			ans = max(ans, now);
		}
		printf("Case #%d: %d\n", cc, ans);
	}
	return 0;
}

