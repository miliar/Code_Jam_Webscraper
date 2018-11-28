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
const int MAXN = 1111;
const int MAXS = 12;
        
int t;
int n, a[MAXN], ans, cans, mx;   

int main() { 
        	
	scanf("%d", &t);
		
	forn(tt, t) {
		scanf("%d", &n);
		
		mx = -1;
		forn(i, n) {
			scanf("%d", &a[i]);      
			mx = max(mx, a[i]);
		}
		
		ans = mx;
		for (int i = 1; i <= mx; i++) {
			cans = i;
			forn(j, n)
				cans += (a[j] - 1) / i;
			ans = min(ans, cans);
		}
				                              
		printf("Case #%d: %d\n", tt + 1, ans);	
	}
	
	return 0;
}