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
const ld eps = 1e-14;
const int INF = 1E9;		                    
const int MAXN = 11111;
        
int t;
ll x, k;
int n, a[MAXN], p[MAXN], m[8][8], inv[8], sum, sum0, res;
ll l, r;
bool f;
string s;  
map<char, int> lib;
          
int main() { 
        	
	m[0][0] = 0; m[0][1] = 1; m[0][2] = 2; m[0][3] = 3;
	m[1][0] = 1; m[1][1] = 4; m[1][2] = 3; m[1][3] = 6;
	m[2][0] = 2; m[2][1] = 7; m[2][2] = 4; m[2][3] = 1;
	m[3][0] = 3; m[3][1] = 2; m[3][2] = 5; m[3][3] = 4;
	forn(i, 4)
		forn(j, 4) {
			m[i + 4][j] = (m[i][j] + 4) % 8;
			m[i][j + 4] = (m[i][j] + 4) % 8;
			m[i + 4][j + 4] = m[i][j];
		}
	inv[0] = 0;
	inv[1] = 5;
	inv[2] = 6;
	inv[3] = 7;
	inv[4] = 4;
	inv[5] = 1;
	inv[6] = 2;
	inv[7] = 3;
	
	lib['i'] = 1;
	lib['j'] = 2;
	lib['k'] = 3;
	
	scanf("%d", &t);
	forn(tt, t) {
		cin >> n >> x; 
		cin >> s;
		forn(i, n)
			a[i] = lib[s[i]];
		f = 1;
		
		sum0 = 0;
		forn(i, n)
			sum0 = m[sum0][a[i]];
		//cout << a[0] << a[1] << '\n';
		//cout << sum0 << '\n';
			
		sum = 0;
		k = x % 4;
		forn(i, k)
			sum = m[sum][sum0];
		//cout << sum << '\n';
			
		res = 0;
		res = m[inv[1]][sum];
		res = m[res][inv[3]];
		
		if (res != 2)
			f = 0;
		//cout << 1 << ' ' << f << '\n';
		
		l = 0;
		res = 0;
		forn(i, 4 * n) {
			res = m[res][a[l % n]];
			if (res == 1)
				break;
			l++;
		}
		if (res != 1)
			f = 0;
		//cout << 2 << ' ' << f << '\n';
		
		r = x * n - 1; 
		res = 0;
		forn(i, 4 * n) {
			res = m[a[r % n]][res];
			if (res == 3)
				break;
			r--;
			if (r < 0)
				break;
		}
		if (res != 3)
			f = 0;
		//cout << 3 << ' ' << f << '\n';
		
		if (l >= r)
			f = 0;
		//cout << 4 << ' ' << f << '\n';
				
		printf("Case #%d: ", tt + 1);
		cout << (f ? "YES\n" : "NO\n");	
	}
	
	return 0;
}