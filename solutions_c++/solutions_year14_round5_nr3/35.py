#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;
typedef long long i64;

int N, idtype;
bool ty[1010]; int id[1010];

bool dp[2][1<<15];

int main()
{
	int T;
	scanf("%d", &T);

	for(int ta = 0; ta++ < T; ) {
		scanf("%d", &N);
		vector<int> ids;

		for(int i = 0; i < N; i++) {
			char in[5]; int v;
			scanf("%s%d", in, &v);

			ty[i] = (in[0] == 'E' ? true : false);
			id[i] = v;

			if(id[i] != 0) ids.push_back(id[i]);
		}

		ids.push_back(0);
		sort(ids.begin(), ids.end());
		ids.erase(unique(ids.begin(), ids.end()), ids.end());

		for(int i = 0; i < N; i++) {
			if(id[i] != 0) id[i] = lower_bound(ids.begin(), ids.end(), id[i]) - ids.begin();
		}

		int t = 0;

		for(int i = 0; i < (1<<15); i++) dp[t][i] = true;

		for(int i = 0; i < N; i++) {
			for(int j = 0; j < (1<<15); j++) dp[1-t][j] = false;
			//printf("%d %d\n", ty[i], id[i]);

			for(int j = 0; j < (1<<15); j++) {
				if(id[i] == 0) {
					for(int k = 0; k < 15; k++) {
						if(ty[i]) {
							if(!(j & (1<<k))) dp[1-t][j | (1<<k)] |= dp[t][j];
						}else{
							if(j & (1<<k)) dp[1-t][j ^ (1<<k)] |= dp[t][j];
						}
					}
				} else {
					int p = id[i] - 1;

					if(ty[i]){
						if(!(j & (1<<p))) dp[1-t][j | (1<<p)] |= dp[t][j];
					}else{
						if(j & (1<<p)) dp[1-t][j ^ (1<<p)] |= dp[t][j];
					}
				}
			}

			t = 1-t;
		}

		int ret = 100;
		for(int i = 0; i < (1<<15); i++) if(dp[t][i]) {
			int cnt = 0;
			for(int j=0;j<15;j++) if(i&(1<<j)) ++cnt;

			ret = min(ret, cnt);
		}
		if(ret == 100) printf("Case #%d: CRIME TIME\n", ta);
		else printf("Case #%d: %d\n", ta, ret);
	}

	return 0;
}
