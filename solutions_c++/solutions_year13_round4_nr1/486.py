#include <cstdio>
#include <algorithm>


inline long long min(long long a, long long b) { return a < b? a: b; }
inline long long F(long long a) {
	return a * (a + 1) / 2;
}

struct Eve {
	int pre, pos, typ, val;
	Eve(int x = 0, int p = 0, int t = 0, int v = 0): pre(x), pos(p), typ(t), val(v) {}
	bool operator<(const Eve &cmp) const {
		if(pos != cmp.pos) return pos < cmp.pos;
		else return typ > cmp.typ;
	}
}eve[2001];

int N, M;

long long P[2001], V[2001];
int cnt;

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	//freopen("A-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t) {
		scanf("%d%d", &N, &M);
		for(int i = 0; i < M; ++i) {
			int a, b, c;
			scanf("%d%d%d", &a, &b, &c);
			eve[i * 2] = Eve(a, a, 1, c);
			eve[i * 2 + 1] = Eve(a, b, -1, c);
		}
		M *= 2;
		std::sort(eve, eve + M);
		long long ans = 0;
		cnt = 0;
		for(int i = 0; i < M; ++i) {
			//printf("->%d %d\n", eve[i].pos, eve[i].typ);
			if(eve[i].typ == 1) {
				P[cnt] = eve[i].pos;
				V[cnt] = eve[i].val;
				//printf("++%d: %lld %lld\n", cnt, P[cnt], V[cnt]);
				++cnt;
			} else {
				long long lft = eve[i].val;
				while(lft > 0) {
					long long use = min(lft, V[cnt - 1]);
					lft -= use;
					V[cnt - 1] -= use;
					ans += (F(eve[i].pos - P[cnt - 1]) - F(eve[i].pos - eve[i].pre)) * use;
					//printf("%d %d  %lld %lld: %lld\n", eve[i].pos, eve[i].pre, P[cnt - 1], ans, use);
					if(V[cnt - 1] == 0) --cnt;
				}
			}
		}
		printf("Case #%d: %lld\n", t, ans);
	}
}
