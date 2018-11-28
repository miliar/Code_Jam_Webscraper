#include<iostream> 
#include<cstdio> 
#include<cmath> 
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<ctime>
#include<cassert>
#include<queue>

#define LL long long
#define mp make_pair
#define f first
#define s second
#define pii pair<int, int>
#define pb push_back

using namespace std;

int main() {
	freopen("b.in", "r", stdin);
	freopen(".out", "w", stdout);

	int t;
	cin >> t;

	for (int test = 0; test < t; test++) {
		int n, m;
		cin >> n >> m;

		int maxn[n], maxm[m], cur[n][m], p[n][m];
		for (int i = 0; i < n; i++)
			maxn[i] = 0;
		for (int i = 0; i < m; i++)
			maxm[i] = 0;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				cin >> p[i][j];
				if (maxn[i] < p[i][j])
					maxn[i] = p[i][j];
				if (maxm[j] < p[i][j])
					maxm[j] = p[i][j];
				cur[i][j] = 100;
			}
		
		bool ans = true;
		for (int i = 0; i < n; i++) {
			bool flag = false;
			for (int j = 0; j < m; j++) {
				cur[i][j] = min(cur[i][j], min(maxn[i], maxm[j]));
				if (cur[i][j] != p[i][j]) {
					flag = true;
					ans = false;
					break;
				}
			}
			if (flag)
				break;
		}

		cout << "Case #" << test + 1 << ": ";

		if (ans)
			cout << "YES";
	    else
	    	cout << "NO";
		cout << endl;
	}

	return 0;
}