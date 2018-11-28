#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;

typedef long long LL;

const int MAXM = 2000 + 5;
const LL P = 1000002013;

int n, m;
LL start[MAXM], end[MAXM], people[MAXM];
LL pos[MAXM * 3];
int len;

map<LL, LL> curp;

LL sum(LL start, LL end) {
	LL from = n - (end - start);
	LL to = n - 1;
	return (from + to) * (to - from + 1) / 2;
}

int solve() {
	len = 0;
	for (int i = 0; i < m; ++i) {
		pos[len++] = start[i];
		pos[len++] = end[i];
	}
	sort(pos, pos + len);
	len = unique(pos, pos + len) - pos;

	LL ans = 0;
	curp.clear();
	for (int k = 0; k < len; ++k) {
		for (int i = 0; i < m; ++i) 
			if (start[i] == pos[k]) { 
				if (!curp.count(-start[i])) curp[-start[i]] = 0;
				curp[-start[i]] += people[i];
			}
		for (int i = 0; i < m; ++i) 
			if (end[i] == pos[k]) {
				LL num = people[i];
				while (num > 0) {
					map<LL,LL>::iterator it = curp.begin();
					LL down = min(it->second, num);
					ans += ((down % P) * (sum(-it->first, pos[k]) % P)) % P;
					if (it->second > num) {
						it->second -= num;
						num = 0;
					}
					else {
						num -= it->second;
						curp.erase(it->first);
					}
				}
			}
	}

	LL orig = 0;
	for (int i = 0; i < m; ++i) {
		orig += ((sum(start[i], end[i]) %P ) * (people[i] % P)) % P;
	}
	orig -= ans;
	orig %= P;
	orig = (orig + P ) % P ;
	return (int)(orig % P);
//	return (int)((orig - ans) % 1000002013);
}

int main() {
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		cin >> n >> m;
		for (int i = 0; i < m; ++i) {
			cin >> start[i] >> end[i] >> people[i];
		}
		cout << "Case #" << cs << ": " << solve() << endl;
	}
}
