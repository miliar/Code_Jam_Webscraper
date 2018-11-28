#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 111;

int a[MAXN][MAXN];
bool okc[MAXN], okr[MAXN];
int n, m;
bool check(int h) 
{
	memset(okr, 0, sizeof(okr));
	memset(okc, 0, sizeof(okc));
	for (int i = 1; i <= n; ++i)
	{
		okr[i] = true;
		for (int j = 1; j <= m; ++j)
			okr[i] &= a[i][j] <= h;
	}
	for (int j = 1; j <= m; ++j)
	{
		okc[j] = true;
		for (int i = 1; i <= n; ++i)
			okc[j] &= a[i][j] <= h;
	}
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			if (a[i][j] <= h)
				if (!okr[i] && !okc[j])
					return false;
	return true;
}
int main()
{
	int cases;
	cin >> cases;
	for (int tcase = 1; tcase <= cases; ++tcase) {
		cout << "Case #" << tcase << ": ";
		cin >> n >> m;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= m; ++j)
				cin >> a[i][j];
		bool flag = true;
		for (int i = 1; i <= 100; ++i)
			if (!check(i)) {
				flag = false;
				break;
			}
		if (flag) cout << "YES" << endl;
		 else cout << "NO" << endl;
	}
	return 0;
}

