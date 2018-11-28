#include <bits/stdc++.h>

using namespace std;

template<class T> inline bool _min(T& data, const T& comp) {
	if (comp < data) {
		data = comp;
		return true;
	}
	return false;
}

template<class T> inline bool _max(T& data, const T& comp) {
	if (data < comp) {
		data = comp;
		return true;
	}
	return false;
}

long n;

bool mp[4][4];
bool sim[4][4];
bool checked[4];

bool check(long who) {
	if (checked[who]) return true;
	set<long> man{who};
	assert(man.size() == 1);
	set<long> job;
	for (bool flag = true; flag;) {
		flag = false;
		for (const auto &x : man) {
			for (long i = 0; i < n; ++ i) {
				if (sim[x][i] && job.find(i) == job.end()) {
					job.insert(i);
					flag = true;
				}
			}
		}
		for (const auto &x : job) {
			for (long i = 0; i < n; ++ i) {
				if (sim[i][x] && man.find(i) == man.end()) {
					man.insert(i);
					flag = true;
				}
			}
		}
	}

	if (man.size() != job.size()) return false;
	for (const auto &x : man) {
		checked[x] = true;
		for (const auto &y : job) {
			if (!sim[x][y]) return false;
		}
	}
	return true;
}

void f(long patt) {
	for (long now = 0; now < n * n; ++ now)
		sim[now / n][now % n] = (patt >> now) & 1;
}

int main(void) {
	ios::sync_with_stdio(false);

	long T;
	scanf("%ld", &T);
	for (long t = 1; t <= T; ++ t) {
		scanf("%ld", &n);
		for (long i = 0; i < n; ++ i) {
			static char buff[1024];
			scanf("%s", buff);
			for (long j = 0; j < n; ++ j) {
				mp[i][j] = buff[j] == '1';
			}
		}

		printf("Case #%d: ", t);

		// For small only
		
		if (n == 1) {
			printf("%d\n", mp[0][0] == 0);
		} else {
			long l = n * n, ans = 0x3F3F3F3F;
			for (long i = 0; i < (1 << l); ++ i) {
				f(i);
				bool flag = true;
				long cur = 0;
				for (long x = 0; x < n; ++ x) {
					for (long y = 0; y < n; ++ y) {
						if (mp[x][y] != sim[x][y]) {
							if (mp[x][y]) {
								flag = false;
								break;
							}
							++ cur;
						}
						if (!flag) break;
					}
				}
				if (cur >= ans) continue;
				if (!flag) continue;
				memset(checked, 0, sizeof checked);
				for (long x = 0; x < n; ++ x) {
					if (!check(x)) {
						flag = false;
						break;
					}
				}
				if (!flag) continue;
				_min(ans, cur);
			}
			printf("%ld\n", ans);
		}
	}

	return 0;
}
