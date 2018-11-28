#include <bits/stdc++.h>

#define sz(a) int((a).size())
#define tr(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(),(c).end()
#define uniq(c) sort(all((c))); (c).resize(unique(all((c))) - (c).begin())
#define lobo(c, x) (int) (lower_bound(all((c)), (x)) - (c).begin())
#define upbo(c, x) (int) (upper_bound(all((c)), (x)) - (c).begin())
#define R(i,a,b) for (int i=a; i<=b; i++)
#define Re(i,a,b) for (int i=a; i>=b; i--)
#define stop getchar();
#define tess puts("===========");
#define tes(a) cerr<< #a << " = "<< a <<endl;
#define cincout ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);

#define pb  push_back
#define mp  make_pair
#define endl "\n"

#define fi  first
#define se  second
#define x   first
#define y   second
#define between(a,b,c) ((a) >= (b) and (a) <= (c))
using namespace std;
typedef long long int64;


int main(int argc, char const *argv[])
{
	cincout;
	int T;
	cin >> T;
	R(tc,1,T) {
		string s; int k;
		int ans = 0;

		cin >> s >> k;
		R(i,0,sz(s)-k) if (s[i] != '+') {
			R(j,i,i+k-1) s[j] = s[j] == '+' ? '-' : '+';
			ans++;
			// cout << s << " " << ans << endl;
		}
		R(i,0,sz(s)-1) if (s[i] == '-') ans = -1;

		cout << "Case #" << tc << ": ";
		cout << (ans == -1 ? "IMPOSSIBLE" : to_string(ans)) << endl;
	}
	return 0;
}