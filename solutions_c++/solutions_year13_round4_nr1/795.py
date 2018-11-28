#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 2005;
const int Mod = 1000002013;
struct Node {
	int l, r, w;
	Node(int l, int r, int w):l(l), r(r), w(w){}
	bool operator < (const Node &oth) const {
		return l < oth.l || (l == oth.l && r < oth.r) || (l == oth.l && r == oth.r && w < oth.w);
	}
};
typedef pair <int,int> PII;
int Tc;
int n, m;
map < pair <int,int>, int > mp, res;
typedef map <PII, int>::iterator iter;

void add(int &cur, int w) {
	cur += w;
	cur %= Mod;
}

long long calc(long long m) {
	return (n + (n - m + 1)) * m / 2 % Mod;
}
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
int main() {
	scanf("%d", &Tc);
	rep (ri, Tc) {
		printf("Case #%d: ", ri + 1);
		mp.clear();
		res.clear();
		scanf("%d%d", &n, &m);
		long long ori = 0;
		rep (i, m) {
			int l, r, w;
			scanf("%d%d%d", &l, &r, &w);
			ori = ori + (long long)calc(r - l) % Mod * w % Mod;
			ori %= Mod;
			add(mp[make_pair(l, r)], w);
		}
		int cnt = m;
		while (!mp.empty()) {
			bool flag = 0;
			iter _st = mp.begin();
			for (iter _it = mp.begin(); _it != mp.end(); _it++) {
					const PII *st = &(_st->first);
					const PII *it = &(_it->first);
					if (st->first < it->first && it->first <= st->second && st->second < it->second) {
						flag = 1;
						Node r0(st->first, it->second, min(_st->second, _it->second));
						Node r1(it->first, st->second, min(_st->second, _it->second));
						Node r2 = _st->second > _it->second ? Node(st->first, st->second, _st->second - _it->second) : Node(it->first, it->second, _it->second - _st->second);
						mp.erase(_st);
						mp.erase(_it);
						if (r0.l != r0.r && r0.w) add(mp[make_pair(r0.l, r0.r)], r0.w);
						if (r1.l != r1.r && r1.w) add(mp[make_pair(r1.l, r1.r)], r1.w);
						if (r2.l != r2.r && r2.w) add(mp[make_pair(r2.l, r2.r)], r2.w);
						break;
					}
			}
			if (!flag) {
				res.insert(*_st);
				mp.erase(_st);
			}
		}
		set < pair <int,int> > s;
		long long ans = 0;
		for (iter it = res.begin(); it != res.end(); it++) {
			ans += calc(it->first.second - it->first.first) % Mod * it->second % Mod;
			ans %= Mod;
		}
		//cout << res.size() << endl;
		cout << (ori - ans + Mod) % Mod << endl;
	}
}
