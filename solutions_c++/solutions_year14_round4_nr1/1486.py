//Template

// By Anudeep :)
//Includes
#include <vector> 
#include <queue>
#include <map> 
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream> 
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
using namespace std;

//M lazy ;)
typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)

#define gi(n) scanf("%d",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
#define dg(n,s); printf("%s %d",s,n)
#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()

int cnt[1024];
int main() {
	int t; gi(t);
	rep(T, t) {
		int n, x;
		gi(n); gi(x);
		memset(cnt, 0, sizeof cnt);
		rep(i, n) {
			int u; gi(u);
			cnt[u]++;
		}
		int ans = 0;
		rep(i, x+1) if(cnt[i]) {
			int j = x - i;
			while(j>i) {
				int lc = min(cnt[i], cnt[j]);
				cnt[i] -= lc;
				cnt[j] -= lc;
				ans += lc;
				j--;
			}
			if(cnt[i] && i+i <= x) ans += (cnt[i]+1)/2, cnt[i] = 0;
			if(cnt[i]) ans += cnt[i], cnt[i] = 0;
		}
		printf("Case #%d: %d\n", T+1, ans);
	}
}