#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

ull n;
int test;

int main ()
	{
		ios :: sync_with_stdio(false);
		cin.tie(0);

		cin >> test;
		int t = test;

		while (test--)
			{
				cout << "Case #" << t - test << ':' << ' ';
				cin >> n;

				if (n == 0)
					{
						cout << "INSOMNIA" << endl;
						continue;
					}
				int ok[10];
				for (int i = 0; i < 10; i++) ok[i] = 0;
				int cnt = 0;
				ull mul = 1;

				while (cnt < 10)
					{
						ull tmp = n * mul;
						while (tmp)
							{
								int x = tmp % 10;
								if (!ok[x])
									{
										ok[x] = 1;
										cnt++;
									}
								tmp /= 10;
							}

						mul++;
					}

				cout << n * (mul - 1) << endl;
			}
		return 0;
	}
