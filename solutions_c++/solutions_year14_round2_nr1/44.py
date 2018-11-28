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

int solve( vi a ) {
	int ans = imax;
	fu(x, 1, 110) {
		int cur = 0;
		rep(i, a.sz) cur += abs(x - a[i]);
		if(cur < ans) ans = cur;
	}
	return ans;
}

string s[110];
string remove(string s) {
	string t = "";
	rep(i, s.ln+1) {
		if(i == s.ln || (i && s[i] != s[i-1])) t += s[i-1];
	}
	return t;
}
int main() {
	int t; gi(t);
	rep(T, t) {
		int n; gi(n);
		rep(i, n) cin >> s[i];
		string st = remove(s[0]);
		bool win = true;
		rep(i, n) if(remove(s[i]) != st) {
			win = false;
			break;
		}
		if(!win) {
			printf("Case #%d: Fegla Won\n", T+1);
			continue;
		}
		int ans = 0;
		rep(i, st.ln) {
			vi a(n, 0);
			rep(j, n) {
				int k = 0;
				while(k<s[j].ln && s[j][k] == st[i]) a[j]++, k++;
				if(k < s[j].ln) s[j] = s[j].substr(k);
			}
			ans += solve(a);
		}
		printf("Case #%d: %d\n", T+1, ans);
	}
	return 0;
}