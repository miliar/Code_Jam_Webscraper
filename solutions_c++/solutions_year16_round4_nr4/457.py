#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#include <limits>
#include <functional>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

int bipartiteMatching(const vector<vector<int> > &g) {
	int nleft = g.size(), nright = 0;
	each(es, g) if(!es->empty()) nright = max(nright, *max_element(es->begin(), es->end()) + 1);
	vi matchL(nleft, -1), matchR(nright, -1), prev(nleft), seen(nleft, -1);
	rep(i, nleft) {
		vi stk; stk.push_back(i);
		seen[i] = i; prev[i] = -1;
		while(!stk.empty()) {
			int v = stk.back(); stk.pop_back();
			each(ui, g[v]) {
				int u = *ui;
				int j = matchR[u];
				if(j == -1) {
					while(v != -1) {
						matchR[u] = v;
						swap(u, matchL[v]);
						v = prev[v];
					}
					goto break_;
				} else if(seen[j] < i) {
					seen[j] = i; prev[j] = v;
					stk.push_back(j);
				}
			}
		}
	break_:;
	}
	return (int)matchL.size() - count(matchL.begin(), matchL.end(), -1);
}


int main() {
	int T;
	scanf("%d", &T);
	for(int ii = 0; ii < T; ++ ii) {
		int N;
		scanf("%d", &N);
		vector<int> masks(N);
		int base = 0;
		rep(i, N) {
			char buf[26];
			scanf("%s", buf);
			rep(j, N) {
				base += buf[j] == '1';
				masks[i] |= (buf[j] == '1') << j;
			}
		}
		int ans = INF;
		vector<vi> g;
		rep(s, 1 << (N * N)) {
			bool ok = true;
			int newm[4];
			int cost = 0;
			rep(i, N * N)
				cost += s >> i & 1;
			rep(i, N) {
				newm[i] = s >> (N * i) & ((1 << N) - 1);
				ok &= (newm[i] & masks[i]) == masks[i];
				ok &= newm[i] != 0;
			}
			if(!ok) continue;
			rep(i, N) {
				//自分以外を使えるマッチングの右側の頂点集合としてありえるのは全部ありえる
				//そのどれかに完全に含まれてたらだめ
				//マトロイドだから、階層的
				//つまり、自分のmaskが自分以外を使う右側の頂点集合としてありえるかどうか
				int mask = newm[i];
				if(mask == (1 << N) - 1) continue;
				g.clear();
				rep(j, N) if(mask >> j & 1) {
					g.push_back(vi());
					rep(k, N) if(k != i && (newm[k] >> j & 1))
						g.back().push_back(k);
				}
				ok &= bipartiteMatching(g) != g.size();
			}
			if(ok)
				amin(ans, cost - base);
		}
		printf("Case #%d: %d\n", ii + 1, ans);
	}
	return 0;
}
