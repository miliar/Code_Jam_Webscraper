#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	freopen("C:/1.txt", "r", stdin);
	freopen("C:/2.txt", "w", stdout);
	int ttt;
	cin >> ttt;
	for (int go=1;go<=ttt;++go)
	{
		cout << "Case #" << go << ": ";
		int n, m, h[111][111];
		cin >> n >> m;
		for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) cin >> h[i][j];
		for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j)
		{
			{ bool d=1; for (int k = 0; k < n; ++k) if (h[k][j]>h[i][j]) d=0; if (d) continue; }
			{ bool d=1; for (int k = 0; k < m; ++k) if (h[i][k]>h[i][j]) d=0; if (d) continue; }
			goto no;
		}
		cout <<  "YES\n"; goto ex; no: cout << "NO\n"; goto ex; ex: ;
	}
	return 0;
}
