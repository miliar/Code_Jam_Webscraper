#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iostream>
using namespace std;
typedef long long LL;
const int MOD = 1000002013;
map<int, LL> ma, num;
map<int, LL> :: iterator it;
map<int, LL> :: reverse_iterator rit;
int main() {
	int testnum;
	int n, m, I, O, cnt, tot, ntot;
	scanf("%d", &testnum);
	for (int test = 1; test <= testnum; test++) {	
		ma.clear();
		scanf("%d%d", &n, &m);
		tot = 0;
		for (int i = 0; i < m; i++) {
			scanf("%d%d%d", &I, &O, &cnt);
			ma[I] += cnt;
			ma[O] -= cnt;
			if ((O - I) & 1)
				tot = (tot + ((((2LL * n - O + I + 1) >> 1) * (O - I)) % MOD) * cnt) % MOD;
			else
				tot = (tot + (((LL)((O - I) >> 1) * (2LL * n - O + I + 1)) % MOD) * cnt) % MOD;
		}
		ntot = 0;
		num.clear();
		for (it = ma.begin(); it != ma.end(); it++) {
			if (it->second > 0) {
				num[it->first] = it->second;
			} else if (it->second < 0) {
				LL drop = -it->second;
				vector<int> v;
				for (rit = num.rbegin(); rit != num.rend() && drop > 0; rit++) {
					LL td = min(drop, rit->second);
					int seg = it->first - rit->first;
					if (seg & 1)
						ntot = (ntot + ((((2LL * n - seg + 1) >> 1) * seg) % MOD) * td) % MOD;
					else
						ntot = (ntot + (((LL)(seg >> 1) * (2LL * n - seg + 1)) % MOD) * td) % MOD;
					drop -= td;
					rit->second -= td;
					if (rit->second == 0) v.push_back(rit->first);
				}
				for (int i = 0; i < (int)v.size(); i++)
					num.erase(v[i]);
			}
		}
		printf("Case #%d: %d\n", test, (tot + MOD - ntot) % MOD);
	}
	return 0;
}