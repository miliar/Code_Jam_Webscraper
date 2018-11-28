#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<cstdlib>
#include<iostream>
#include<map>
#include<string>
#include<set>
#include<bitset>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<algorithm>
using namespace std;

#define PB push_back
#define MP make_pair
#define SIZE(X) (int)(X).size()

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, l, h) for(int i = (l); i < (h); i++)
#define RREP(i, n) for(int i = (int)(n-1); i >= 0; i--)
#define FORD(i, l, h) for(int i = (int)(h-1); i >= (l); i--)

typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string>VS;
typedef pair<int, int> PII;
typedef vector<PII> VII;
typedef long long ll;

const ll oo = (1LL)<<40;
const int MAXN = 110;
const int MOD = 1000000007;
int n;
int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	int a[4][4], b[4][4];
	int r1, r2;
	freopen("a-small.in", "r", stdin);
	freopen("a-small.out", "w", stdout);
	cin >> T;
	FOR(_, 1, T+1) {
		cin >> r1;
		REP(i, 4) REP(j, 4) cin >> a[i][j];
		cin >> r2;
		REP(i, 4) REP(j, 4) cin >> b[i][j];
		r1--; r2--;
		int cnt = 0, res ;
		REP(i, 4) REP(j, 4) {
			if(a[r1][i] == b[r2][j]){
				cnt++;
				res = a[r1][i];
			}
		}
		cout << "Case #" << _ << ": ";
		if(cnt == 0) cout << "Volunteer cheated!\n";
		else if(cnt == 1) cout << res << endl;
		else cout << "Bad magician!\n";
	}
	return 0;
}

