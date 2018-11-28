#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%I64d", &x)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF 1000000
#define MOD 1000000007
#define f first
#define s second
#define EPS 1e-7
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
#define PS push_back
#define M_PI           3.14159265358979323846  /* pi */

int main() {
	Rd;
	Wr;
	int T;
	sc(T);
	loop(t,0,T)
	{
		string str, mini = "";
		cin >> str;
		mini += str[0];
		loop(i,1,str.size())
		{
			if (str[i] != mini[mini.size() - 1]) {
				mini += str[i];
			}
		}
		int ans = 0;
		if (mini[0] == '-')
			ans++;
		loop(i,1,mini.size())
		{
			if (mini[i] == '-') {
				ans += 2;
			}
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}
