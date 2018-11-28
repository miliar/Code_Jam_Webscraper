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
const int MAXN = 100500;
const string code = "PRS";
const int par[3][2] = {{0, 1}, {1, 2}, {0, 2}};

int tt, n;
int num[3], cnt[3];
bool ok;
string cur, res;

string gen(int lvl, int winner) {
	if (lvl == n) {
		string t = "";
		t += code[winner];
		
		return t;
	}
	
	string s1 = gen(lvl + 1, par[winner][0]);
	string s2 = gen(lvl + 1, par[winner][1]);
	string r1 = s1 + s2;
	string r2 = s2 + s1;
	return min(r1, r2);	
}

int main() {
	
	cin >> tt;
	forn(ttt, tt) {
		scanf("%d", &n);
		scanf("%d %d %d", &num[1], &num[0], &num[2]);

		printf("Case #%d: ", ttt + 1);
		 	
		ok = 0;
		forn(i, 3) {
			cur = gen(0, i);

			assert((int)cur.size() == (1 << n));
			memset(cnt, 0, sizeof(cnt));
			
			forn(j, cur.size())
				forn(k, 3)
					if (cur[j] == code[k])
						cnt[k]++;

			bool corr = 1;
			forn(j, 3)
				if (cnt[j] != num[j]) {
					corr = 0;
					break;
				}

			if (corr) {
				if (!ok) {
					ok = 1;
					res = cur;
				} else
					res = min(res, cur);
			}
		}
		
		if (!ok)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		cout << '\n';
	}
		
	return 0;
}                