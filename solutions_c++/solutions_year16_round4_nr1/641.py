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

string solve(int i, int t, int xs[3]) {
	if(i == 0) {
		-- xs[t];
		return string(1, "RPS"[t]);
	}
	int x = t, y = (t + 2) % 3;
	string a = solve(i - 1, x, xs);
	string b = solve(i - 1, y, xs);
	return min(a + b, b + a);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int ii = 0; ii < T; ++ ii) {
		int N; int R; int P; int S;
		scanf("%d%d%d%d", &N, &R, &P, &S);
		string ans = "~";
		rep(k, 3) {
			int xs[3] = { R, P, S };
			string s = solve(N, k, xs);
			if(count(xs, xs + 3, 0) == 3)
				amin(ans, s);
		}
		printf("Case #%d: ", ii + 1);
		if(ans == "~")
			puts("IMPOSSIBLE");
		else
			puts(ans.c_str());
	}
	return 0;
}
