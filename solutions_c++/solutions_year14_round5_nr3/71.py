#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
using namespace std;

const int N = 15;
bool f[1 << N], g[1 << N];
char type[N];
int who[N];

int main() {
	int testCount; cin >> testCount;
	for(int testID = 0; testID < testCount; ++testID) {
		int n; cin >> n;
		map<int, int> id;
		for(int i = 0; i < n; ++i) {
			cin >> type[i] >> who[i]; --who[i];
			if(who[i] != -1) {
				if(id.count(who[i]) == 0) id.insert(make_pair(who[i], id.size()));
				who[i] = id[who[i]];
			}
		}
		for(int mask = 0; mask < 1 << n; ++mask) f[mask] = true;
		for(int i = 0; i < n; ++i) {
			memset(g, 0, sizeof g);
			for(int mask = 0; mask < 1 << n; ++mask) if(f[mask]) {
				if(type[i] == 'E') {
					if(who[i] == -1) {
						for(int x = 0; x < n; ++x)
							if((mask & 1 << x) == 0)
								g[mask | 1 << x] = true;
					} else if((mask & 1 << who[i]) == 0) {
						g[mask | 1 << who[i]] = true;
					}
				} else {
					if(who[i] == -1) {
						for(int x = 0; x < n; ++x)
							if((mask & 1 << x) != 0)
								g[mask & ~(1 << x)] = true;
					} else if((mask & 1 << who[i]) != 0) {
						g[mask & ~(1 << who[i])] = true;
					}
				}
			}
			memcpy(f, g, sizeof f);
		}
		int best = n + 1;
		for(int mask = 0; mask < 1 << n; ++mask) if(f[mask])
			best = min(best, __builtin_popcount(mask));
		printf("Case #%d: ", testID + 1);
		if(best == n + 1) puts("CRIME TIME");
		else printf("%d\n", best);
	}
	return 0;
}
