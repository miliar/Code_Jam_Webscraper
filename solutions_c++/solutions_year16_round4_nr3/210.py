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

struct UnionFind {
	vector<int> data;
	void init(int n) { data.assign(n, -1); }
	bool unionSet(int x, int y) {
		x = root(x); y = root(y);
		if(x != y) {
			if(data[y] < data[x]) swap(x, y);
			data[x] += data[y]; data[y] = x;
		}
		return x != y;
	}
	bool findSet(int x, int y) { return root(x) == root(y); }
	int root(int x) { return data[x] < 0 ? x : data[x] = root(data[x]); }
	int size(int x) { return -data[root(x)]; }
};

int main() {
	int T;
	scanf("%d", &T);
	for(int ii = 0; ii < T; ++ ii) {
		int H; int W;
		scanf("%d%d", &H, &W);
		int N = (H + W) * 2;
		vector<int> match(N, -1);
		for(int i = 0; i < N / 2 ; ++ i) {
			int x; int y;
			scanf("%d%d", &x, &y), -- x, -- y;
			match[x] = y;
			match[y] = x;
		}
		vector<int> pos(N);
		int Horizontal = (H + 1) * W, Vertical = (W + 1) * H;
		rep(p, N) {
			int i, j;
			if(p < W) {
				i = 0, j = 1 + p;
				pos[p] = i * W + (j - 1);
			} else if(p < W + H) {
				i = 1 + (p - W), j = W + 1;
				pos[p] = Horizontal + (i - 1) * (W + 1) + (j - 1);
			} else if(p < W + H + W) {
				i = H + 1, j = 1 + (W - 1 - (p - W - H));
				pos[p] = (i - 1) * W + (j - 1);
			} else {
				i = 1 + (H - 1 - (p - W - H - W)), j = 0;
				pos[p] = Horizontal + (i - 1) * (W + 1) + j;
			}
		}
		string ans = "IMPOSSIBLE";
		rep(s, 1 << (H * W)) {
			UnionFind uf;
			uf.init(Horizontal + Vertical);
			rer(i, 1, H) rer(j, 1, W) {
				if(~s >> ((i - 1) * W + (j - 1)) & 1) {
					uf.unionSet((i - 1) * W + (j - 1), Horizontal + (i - 1) * (W + 1) + (j - 1));
					uf.unionSet(i * W + (j - 1), Horizontal + (i - 1) * (W + 1) + j);
				} else {
					uf.unionSet((i - 1) * W + (j - 1), Horizontal + (i - 1) * (W + 1) + j);
					uf.unionSet(i * W + (j - 1), Horizontal + (i - 1) * (W + 1) + (j - 1));
				}
			}
			bool ok = true;
			rep(p, N)
				ok &= uf.findSet(pos[p], pos[match[p]]);
			if(ok) {
				ans = "";
				rep(i, H) {
					rep(j, W)
						ans += "/\\"[s >> (i * W + j) & 1];
					if(i != H - 1)
						ans += '\n';
				}
				break;
			}
		}
		printf("Case #%d:\n", ii + 1);
		puts(ans.c_str());
	}
	return 0;
}
