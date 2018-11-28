#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define vi vector<int>
#define pii pair<int, int>
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second                    
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef long double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int INF = 1E9;        
const int MAXN = 111;
const char dir[4] = {'<', '>', '^', 'v'};
const int dx[4] = {0, 0, -1, 1};
const int dy[4] = {-1, 1, 0, 0};
                                                                             
int t;
int n, m;
string s[MAXN];
int a[MAXN][MAXN], good[4], ans;
bool ok;

int main() {

  	scanf("%d\n", &t);
  	forn(tt, t) {
  		scanf("%d %d\n", &n, &m);
  		forn(i, n)
  			cin >> s[i];

  		forn(i, n)
  			forn(j, m) {
  				a[i][j] = -1;
  				forn(d, 4)
  					if (s[i][j] == dir[d])
  						a[i][j] = d;  				
  			}
  			
  		ans = 0;
  		forn(i, n) {
  			forn(j, m) {
  				if (a[i][j] == -1)
  					continue;

  				forn(d, 4)
  					good[d] = 1;
  				forn(d, 4) {
  					int ci = i, cj = j;
  					while (true) {
  						ci += dx[d];
  						cj += dy[d];

  						if (!(0 <= ci && ci < n && 0 <= cj && cj < m)) {
  							good[d] = 0;
  							break;
  						}
  						if (a[ci][cj] != -1)
  							break;
  					}
  				}
  				
  				ok = 0;
  				forn(d, 4)
  					ok |= good[d];
  				if (!ok) {
  					ans = -1;
  					break;
  				}
  				
  				if (!good[a[i][j]])
  					ans++;
  			}
  			if (!ok)
  				break;
  		}
  		
  		printf("Case #%d: ", tt + 1);
  		if (ans == -1)
  			cout << "IMPOSSIBLE\n";
  		else
  			cout << ans << '\n';
  	}  		    
	return 0;
}