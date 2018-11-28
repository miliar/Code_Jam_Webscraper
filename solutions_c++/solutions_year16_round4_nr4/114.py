#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int INF = 1E9;	
const int MAXN = 25;

int tt, n;
string s[MAXN];
int ans, can[MAXN][MAXN];
int id[MAXN], used[MAXN];

bool isOkay(int pos) {
	if (pos == n)
		return 1;

	bool any = 0;
	for (int i = 0; i < n; i++) {
		if (can[id[pos]][i] && !used[i]) {
			any = 1;
			
			used[i] = 1;
			if (!isOkay(pos + 1))
				return 0;
			used[i] = 0;
		}
	}
	
	if (!any)
		return 0;
		
	return 1;
}

void genAllStates(int i, int j, int curAns) {
	if (i == n) {
		forn(k, n)
			id[k] = k;

		while (true) {
			memset(used, 0, sizeof(used));
			if (!isOkay(0))
				return;
			
			if (!next_permutation(id, id + n))
				break;
		}
		
		if (curAns < ans) {
			ans = curAns;
		/*
			cout << ans << '\n';
			forn(ii, n)
				forn(jj, n)
					cout << can[ii][jj] << " \n"[jj == n - 1];	
		*/
		}
		return;
	}
	
	if (curAns >= ans)
		return;
	
	int ni = i;
	int nj = j + 1;
	if (j == n) {
		ni++;
		nj = 0;
	}
	
	genAllStates(ni, nj, curAns);
	if (!can[i][j]) {
		can[i][j] = 1;
		genAllStates(ni, nj, curAns + 1);
		can[i][j] = 0;
	}
}

int main() {
	
	cin >> tt;
	forn(ttt, tt) {
		cin >> n;
		printf("Case #%d: ", ttt + 1);

		forn(i, n)
			cin >> s[i];
			
		forn(i, n)
			forn(j, n)
				can[i][j] = s[i][j] == '1';
				
		ans = INF;
				genAllStates(0, 0, 0);
		
		printf("%d\n", ans);	
	}
		
	return 0;
}                