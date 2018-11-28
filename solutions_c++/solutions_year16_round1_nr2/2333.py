#include <bits/stdc++.h>
#define MAX_N 55
#define MAX_C 2510

using namespace std;

int test;
int n;
int a[2 * MAX_N][MAX_N];
int cnt[MAX_C];

int main ()
	{
		ios :: sync_with_stdio(false);
		cin.tie(0);

		cin >> test;

		int t = test;

		while (test--)
			{
				cout << "Case #" << t - test << ": ";

				for (int i = 1; i <= MAX_C; i++) cnt[i] = 0;

				cin >> n;

				for (int i = 1; i <= 2 * n - 1; i++)
					for (int j = 1; j <= n; j++)
						{
							int x;
							cin >> x;
							cnt[x]++;
						}

				for (int i = 1; i <= MAX_C; i++)
					if (cnt[i] % 2) cout << i << ' ';

				cout << "\n";
			}
		return 0;
	}
