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

string up[15][3];
int num[15][3][3];

int main() {
    scanf("%d", &TC);

    up[0][0] = "P";
    up[0][1] = "S";
    up[0][2] = "R";

    rep(i, 3) num[0][i][i] = 1;

    for (int i = 1; i <= 12; ++i) {
	rep(j, 3) {
	    int a = j, b = (j + 1) % 3;
	    rep(k, 3) num[i][j][k] = num[i - 1][a][k] + num[i - 1][b][k];
	    up[i][j] = min(up[i - 1][a] + up[i - 1][b], up[i - 1][b] + up[i - 1][a]);
	}
    }

    for (int tc = 1; tc <= TC; ++tc) {
	printf("Case #%d: ", tc);
	
	int N, P, R, S;
	scanf("%d %d %d %d", &N, &R, &P, &S);

	string ans;
	bool f = 0;

	rep(i, 3) {
	    if (num[N][i][0] == P && num[N][i][1] == S && num[N][i][2] == R) {
		if (!f) {
		    ans = up[N][i];
		    f = 1;
		} else ans = min(ans, up[N][i]);
	    }
	}
	if (!f) ans = "IMPOSSIBLE";
	cout << ans << endl;
    }

    return 0;
}
