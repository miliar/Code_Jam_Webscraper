#include <cstring>
#include <map>
#include <numeric>
#include <sstream>
#include <cmath>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <queue>
#include <string>
#include <cctype>

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb(x) push_back((x))
#define REP(i,x,y) for(int i = x; i < int(y); i++)
#define FOR(it,A) for(typeof (A.begin()) it = A.begin(); it!= A.end(); it++)
#define CUA(x) (x) * (x)
#define mp(x,y) make_pair((x),(y))
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
#define I (1LL << 40)
#define sz size()
#define oo (1<<30)
#define EPS (1e-9)

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<pii> vii;
typedef vector<string> vs;
typedef vector<int> vi;

const int hi[] = {0, 0, 1, -1};
const int hj[] = {1, -1, 0, 0};
const char sym[] = {'>', '<', 'v', '^'};

char s[200][200];

int main() {
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		//freopen("output.txt","w",stdout);
	#endif	
    int ct;
    int r, c;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++) scanf("%s", s[i]);
        int res = 0;
        for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (s[i][j] == '.') continue;
				if (res == -1) break;
				bool ok = false;
				bool ok2 = false;
				for (int k = 0; k < 4; k++) {
					bool ok3 = false;
					int ii = i + hi[k], jj = j + hj[k];
					while (ii >= 0 && ii < r && jj >= 0 && jj < c) {
						if (s[ii][jj] != '.') {
							ok3 = true;
							break;
						}
						ii += hi[k];
						jj += hj[k];
					}
					if (ok3) {
						ok2 = true;
						if (sym[k] == s[i][j]) ok = true;
					}
				}
				if (ok2) {
					if (!ok) res++;
				}
				else res = -1;
			}
        printf("Case #%d: ", nt);
        if (res == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", res);
    }
    return 0;
}





