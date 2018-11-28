#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define Fit(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define inf 1000000005
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))
//#define mod 1000000000
#define sz(a) ((int)(a).size())

template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcount(s);}
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define Repd(i,n) for(int i = (n)-1; i >= 0; --i)
#define For(i,a,b) for(int i = (a); i <= (b); ++i)
#define Ford(i,a,b) for(int i = (a); i >= (b); --i)

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
#define eps 1e-9
typedef pair<int, int> II;
template<class T> T gcd(T a, T b){ T r; while (b != 0) { r = a % b; a = b; b = r; } return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
#define PI 2 * acos(0)

#define maxn 400005

int test, n, m;
string s[105];
bool have[105][105];
int a[105][105];

string str = "^>v<";
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};

int cal(char ch){
	Rep(i, 4) if(str[i] == ch) return i;
	return -1;
}

bool inside(int r, int c){
	return r >= 0 && r < n && c >= 0 && c < m;
}

void solve(int itest){
	cout << "Case #" << itest << ": ";
	ms(have, 0);
	cin >> n >> m;
	Rep(i, n) cin >> s[i];
	ms(have, 0);
	ms(a, -1);
	Rep(i, n) Rep(j, m){
		a[i][j] = cal(s[i][j]);
	}

	int res = 0;
	Rep(i, n) Rep(j, m) if(!have[i][j] && a[i][j] != -1){
		int r = i, c = j, h = a[i][j];
		int sr = i, sc = j;
		while(inside(r, c)){
			if(have[r][c]) break;
			else{
				if(a[r][c] == -1){
					r += dr[h];
					c += dc[h];
				} else{
					have[r][c] = 1;
					sr = r;
					sc = c;
					h = a[r][c];
					r += dr[h];
					c += dc[h];
				}
			}
		}

		if(!inside(r, c)){
			bool ok = false;
			Rep(i, n) if(i != sr && a[i][sc] != -1){
				ok = true;
			}
			Rep(i, m) if(i != sc && a[sr][i] != -1){
				ok = true;
			}

			if(ok){
				res++;
			} else res = inf;
		}
	}

	if(res >= inf){
		cout << "IMPOSSIBLE" << endl;
	} else cout << res << endl;
}

int main(){

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> test;
    For(itest, 1, test){
    	solve(itest);
    }

    return 0;
}
