#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define X first
#define Y second
#define Sz size()
#define mp make_pair
#define foreach(i, x) for(__typeof((x).begin()) i = (x).begin(); i != (x).end(); i ++)
#define Say(x) cerr << #x << " = " << x << endl
#define For(i, n) for(int i = 0; i < (n); i++)
#define ALL(x) (x).begin(), (x).end()
typedef long long ll;
typedef vector <int> vint;
typedef pair <int,int> pii;

const int M = 100 + 4, Inf = 1e9 + 10;

/////////////////////////////////////////////////////////////////////////

int main()
{
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt ++) {
		string s;
		cin >> s;
		int n = s.length() + 1;
		bool a[n];
		memset(a, 0, sizeof a);
		for (int i = 0; i < n - 1; i ++)
			if (s[i] == '-')
				a[i] = 1;
		int ans = 0;
		while(1) {
			int p = 1;
			for (; p < n; p ++)
				if (a[p] != a[p - 1])
					break;
			if (p == n)
				break;
			ans ++;
			for (int i = 0; i < p; i ++)
				a[i] = !a[i];
		}
		cout << "Case #" << tt + 1 << ": " << ans << endl;
	}
	return 0;
}
