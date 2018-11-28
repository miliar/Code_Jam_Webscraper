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

int main() {
	int T;
	scanf("%d", &T);
	for(int ii = 0; ii < T; ++ ii) {
		string S;
		cin >> S;
//		S.resize(rand() % 8 + 1);
//		rep(i, S.size()) S[i] = "+-"[rand() % 2];

		string orgS = S;
		int ans = 0;
		while(count(all(S), '+') != S.size()) {
			int i = 0;
			char c = S[i];
			for(; i != S.size() && S[i] == c; ++ i)
				S[i] = S[i] == '+' ? '-' : '+';
			reverse(S.begin(), S.begin() + i);
			++ ans;
		}
		printf("Case #%d: %d\n", ii + 1, ans);
		S = orgS;
		/*
		map<string, int> vis;
		vector<string> q, nq;
		int d = 0;
		nq.push_back(S);
		vis.emplace(mp(S, 0));
		while(!nq.empty()) {
			q.swap(nq); nq.clear();
			for(const string &s : q) {
				rer(i, 1, s.size()) {
					string t = string(s.rbegin() + (s.size() - i), s.rend()) + s.substr(i);
					rep(j, i)
						t[j] = t[j] == '+' ? '-' : '+';
					if(vis.emplace(mp(t, d + 1)).second)
						nq.push_back(t);
				}
			}
			++ d;
		}

		int naiveans = vis[string(S.size(), '+')];
		if(naiveans != ans) {
			cerr << S << endl;
			cerr << naiveans << " != " << ans << endl;
		}
		*/
	}
	return 0;
}
