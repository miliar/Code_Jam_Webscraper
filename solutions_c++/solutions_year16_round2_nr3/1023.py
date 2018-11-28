//---------------------------------------------------------------------
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

int const MAX_CH = 8000;
int const MAX_DP_LEN = 1000;
int const MAX_DIFF_COUNT = 50;
long long const LL_INF = 4000000000000000000LL;

int t;
char st[MAX_CH];

pair<string, string> ms[100];
char buf_1[100],buf_2[100];

int dp[1<<17];

struct pp {
	int val,cnt;
} mask[1<<17];
bool operator < (const pp &A, const pp &B) {
	return A.cnt < B.cnt || (A.cnt == B.cnt && A.val < B.val);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	sscanf(st,"%d",&t);
	for (int q=0; q<t; q++) {
		printf("Case #%d: ",q+1);

		gets(st);
		int n;
		sscanf(st,"%d",&n);

		for (int i=0; i<n; i++) {
			gets(st);
			sscanf(st,"%s %s",buf_1,buf_2);
			ms[i].first = buf_1;
			ms[i].second = buf_2;
		}

		for (int i=1; i<(1<<n); i++) {
			int x = i, cnt = 0;
			while (x) {
				cnt += (x%2);
				x/=2;
			}
			mask[i].val = i;
			mask[i].cnt = cnt;
		}

		sort(mask+1,mask+(1<<n));

		for (int i=0; i<(1<<n) ;i++) dp[i] = 0;

		for (int i=1; i<(1<<n); i++) {
			int val = mask[i].val;
			int cnt = mask[i].cnt;

			if (cnt == 1) {
				dp[val] = 0;
				continue;
			}

			for (int j=0; j<n; j++)
				if (!((val >> j) & 1)) {
					int a = 0, b = 0;
					for (int k=0; k<n; k++)
						if ((val>>k)&1) {
							if (ms[k].first == ms[j].first) a = 1;
							if (ms[k].second==ms[j].second) b = 1;
						}
					if (a && b)
						dp[val | (1<<j)] = max(dp[val | (1<<j)], dp[val] + 1);
					else
						dp[val | (1<<j)] = max(dp[val | (1<<j)], dp[val]);
				}

		}

		cout<<dp[(1<<n)-1]<<"\n";
	}
	return 0;
}