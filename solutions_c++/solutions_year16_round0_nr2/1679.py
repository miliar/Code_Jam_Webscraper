/*input
6
-
-+
+-
+++
--+-
-+-+--+
*/
#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ull;
typedef long long int lli;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i = 0; i < n; i++)
#define INF    0x3f3f3f3f
#define NEGINF 0xC0C0C0C0
#define LINF   0x3f3f3f3f3f3f3f3fLL
#define all(v) v.begin(), v.end()
#define NULO -1
#define EPS 1e-10
#define PI 2 * acos(0)
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s))
#define F first
#define S second

inline int cmp(double x, double y = 0, double tol = EPS)
{ return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }

void arquivo()
{
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
}

int main()
{	
	arquivo();
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;
		int ans = 0;

		for(int i = s.size() - 1; i >= 0; i--)
		{
			if(s[i] == '-')
			{
				ans++;
				for(int j = i; j >= 0; j--)
					s[j] = s[j] == '-' ? '+' : '-';
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}