#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <set>
#include <vector>
using namespace std;
const long long MOD = 1000000007;
const int MAX = 200;

int br[MAX], bc[MAX];
int a[MAX][MAX];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	
	for (int t = 0; t < tt; ++t)
	{
		bool res = false;
		int n,m;
		cin >> n  >> m;
		for (int i = 0; i < MAX; ++i)
			br[i] = bc[i] = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> a[i][j];
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				{
				br[i] = max(br[i], a[i][j]);
				bc[j] = max(bc[j], a[i][j]);
				}
	
		res = true;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (a[i][j] != min(bc[j], br[i]))
					res = false;

		cout << "Case #"<< t+1 << ": " << (res ? "YES" : "NO") << endl;		
	}
	return 0;
}