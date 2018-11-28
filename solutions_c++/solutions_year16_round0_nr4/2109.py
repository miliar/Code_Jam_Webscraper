#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T, k, c, s;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> k >> c >> s;
		int cnt = k / c + (k%c > 0);
		cout << "Case #" << t << ": ";
		if (cnt > s) puts("IMPOSSIBLE");
		else {
			int num = 0;
			for (int i = 0; i < cnt;i++)
			{
				__int64 now = 0;
				for (int j = 0; j < c; j++)
				{
					now = now*k + num;
					num = min(num + 1, k - 1);
				}
				cout << now + 1 << ' ';
			}
			cout << endl;
		}
	}
}