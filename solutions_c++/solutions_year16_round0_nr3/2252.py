#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <iostream>

#define ENP     printf("**Entry Point**\n")
#define A       first
#define B       second
#define MP      make_pair

using namespace std;

typedef long long ll;

const int INF = 0x60000000;
const int MINF = -1000000000;
const ll mod = 1000000007;
const int cons = 50000001;
const double pi = 3.141592653589793;

int dat[10][31];
int dat2[10];
vector <vector <int> > ans;
vector <int> tmp;

bool proc(int a, int b, int c, int even, int odd, int n)
{
	if (even == 4 && odd == 4)
	{
		int t1 = (a + dat2[2]) % 5;
		int t2 = (b + dat2[4]) % 5;
		int t3 = (c + dat2[8]) % 5;

		if (!t1 && !t2 && !t3)
		{
			ans.push_back(tmp);
		}

		if (ans.size() == 500)return true;
		return false;
	}
	if (even > 4 || odd > 4)return false;

	for (int i = n; i <= 30; i++)
	{
		tmp.push_back(i);
		if (proc(a + dat[2][i], b + dat[4][i], c + dat[8][i], even + (i % 2 == 0 ? 1 : 0), odd + (i % 2 ? 1 : 0), i + 1))return true;
		tmp.pop_back();
	}
	
	return false;
}

bool isPossible(int x)
{
	int even = 0;
	int odd = 0;
	int tmp = 0;

	while (x)
	{
		if (x & 1)
		{
			if (tmp % 2)
			{
				odd++;
			}
			else
			{
				even++;
			}
		}

		x >>= 1;
		tmp++;
	}

	return even == odd;
}

ll toBaseX(int x, int base)
{
	ll ret = 0;
	ll tmp = 1;

	while (x)
	{
		if (x & 1)
		{
			ret += tmp;
		}

		x >>= 1;
		tmp *= (ll)base;
	}

	return ret;
}

string toStr(int x)
{
	string ret;

	while (x)
	{
		if (x & 1)
		{
			ret += "1";
		}
		else
		{
			ret += "0";
		}

		x >>= 1;
	}

	reverse(ret.begin(), ret.end());

	return ret;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	for (int i = 0; i < 10; i++)
	{
		if (i != 2 && i != 4 && i != 8)continue;

		dat[i][1] = i;
		for (int j = 2; j <= 30; j++)
		{
			dat[i][j] = (dat[i][j - 1] * i) % 10;
		}
	}

	dat2[2] = 9;
	dat2[4] = 5;
	dat2[8] = 3;

	proc(0, 0, 0, 0, 0, 1);

	int testCases;
	scanf("%d", &testCases);

	for (int testNum = 1; testNum <= testCases; testNum++)
	{
		printf("Case #%d:\n", testNum);
		int n, j;
		scanf("%d%d", &n, &j);

		if (n == 16 && j == 50)
		{
			int arr[4] = { 2,4,6,8 };
			int brr[4];
			int cnt = 0;

			int lim = 1 << 16;
			for (int i = (1 << 15); i < lim; i++)
			{
				if (i % 2 == 0)continue;
				int tmp = 0;
				if (isPossible(i))
				{
					ll x[4];
					tmp = 0;
					for (int j = 0; j < 4; j++)
					{
						x[j] = toBaseX(i, arr[j]);
						ll sqrtx = (ll)sqrt(x[j]);

						for (int k = 3; k <= (int)sqrtx; k+= 2)
						{
							if (x[j] % (ll)k == 0)
							{
								brr[j] = k;
								tmp |= (1 << j);
								break;
							}
						}
					}
				}

				if (tmp == ((1 << 4) - 1))
				{
					cnt++;
					string r = toStr(i);
					int a[10] = {0, brr[0], 2, brr[1], 2, brr[2], 2, brr[3], 2, 11 };
					
					cout << r << " ";
					for (int i = 1; i < 10; i++)
					{
						printf("%d ", a[i]);
					}puts("");
				}

		//		printf("%d\n", cnt);
				if (cnt == 50)break;
			}
		}
		else if(n == 32 && j == 500)
		{
			int a[11] = { 0, 0, 5, 2, 5, 2, 5, 2, 5, 2, 11 };

			for (int i = 0; i < ans.size(); i++)
			{
				string res = "10000000000000000000000000000001";

				for (int j = 0; j < ans[i].size(); j++)
				{
					res[res.length() - 1 - ans[i][j]] = '1';
				}

				cout << res << " ";

				for (int j = 2; j < 11; j++)
				{
					printf("%d ", a[j]);
				}puts("");
			}
		}
		else
		{
			puts("-1");
			return 0;
		}
	}

	return 0;
}