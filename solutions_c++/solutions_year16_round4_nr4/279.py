#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

int TC;

int N;
string s[32];
bool g[32][32];
int pm[4];
int f[32];

bool dfs(int p, int st)
{
    if (p == N) {
	if ((st + 1) == (1 << N)) return true;
	else return false;
    }

    int id = pm[p];

    int u = N + 1;
    int bit = f[id];

    if ((st | bit) == st) return false;

    int c = 0;
    rep(i, N) if ((f[id] >> i) & 1) {
	if ((st >> i) & 1) continue;
	++c;
	if (!dfs(p + 1, st | (1 << i))) return false;
    }
    if (c==0)

    return true;
}

int main() {
    scanf("%d", &TC);

    for (int tc = 1; tc <= TC; ++tc) {
	scanf("%d", &N);

	rep(i, N) {
	    cin >> s[i];

	    rep(j, N) {
		g[i][j] = s[i][j] == '1';
	    }
	}

	int ret = N * N;

	rep(i, 1 << (N * N)) {
	    int nc = 0;
	    bool ok = 1;

	    rep(j, N) {
		f[j] = 0;

		rep(k, N) {
		    int ss = (i >> (j * N + k)) & 1;
		    if (ss == 0 && g[j][k]) {
			ok = 0;
			break;
		    }
		    nc += (ss != g[j][k]);

		    if (ss) f[j] |= (1 << k);
		}
	    }

	    if (!ok) continue;

	    rep(j, N) pm[j] = j;

	    bool fl = 1;
	    do {
		if (!dfs(0, 0)) fl = 0;
	    } while (next_permutation(pm, pm + N));

	    if (fl) ret = min(ret, nc);
	}


	printf("Case #%d: %d\n", tc, ret);
    }

    return 0;
}
