#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define XX first
#define YY second

const int MOD = 1e9 + 7;
const int INF = 1e9 + 9;
const int N = 25 + 7;

string s[N];
bool c[N][N];
int p[N];
vector<int> mark[N];

int main()
{
	ios::sync_with_stdio(false);
	for (int i=0; i<N; i++)
		p[i] = i;
	int __;
	cin >> __;
	for (int _=0; _<__; _++)
	{
		cout << "Case #" << _+1 << ": ";

		int n;
		cin >> n;
		for (int i=0; i<n; i++)
			cin >> s[i];
		int ans = n*n;
		for (int i=0; i<1<<(n*n); i++)
		{
			int out = 0;
			bool flag = true;
			for (int j=0; j<n*n; j++)
				if ((i >> j) & 1)
				{
					if (s[j/n][j%n] != '1')
						out++;
					c[j/n][j%n] = 1;
				}
				else
				{
					if (s[j/n][j%n] == '1')
						flag = false;
					c[j/n][j%n] = 0;
				}
			if (!flag)
				continue;
			do
			{
				int ok = 0;
				for (int j=0; j<n; j++)
					mark[j].clear();
				for (int j=0; j<n; j++)
				{
					int th = p[j];
					vector<int> v;
					for (int k=0; k<n; k++)
						if (c[th][k])
							v.push_back(k);
					bool match = true;
					int cc = v.size();
					for (int k=0; k<1<<cc; k++)
					{
						set<int> st;
						for (int l=0; l<cc; l++)
							if ((k >> l) & 1)
								for (auto x : mark[v[l]])
									st.insert(x);
						if (st.size() < __builtin_popcount(k))
							match = false;
					}
					if (!match)
					{
						ok++;
						for (auto x : v)
							mark[x].push_back(th);
					}
				}
				if (ok != n)
					flag = false;
			}while (next_permutation(p, p+n));
			if (flag)
				ans = min(ans, out);
		}
		cout << ans << "\n";
	}

	return 0;
}
