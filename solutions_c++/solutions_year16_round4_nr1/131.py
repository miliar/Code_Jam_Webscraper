#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <string>

#include <valarray>
#include <complex>
#include <functional>

using namespace std;

int n, R, P, S;

void read()
{
	scanf("%d%d%d%d", &n, &R, &P, &S);
}

const int N = 100;
vector <int> produce[N][3];
string str[N][3];

const char REPR[] = {'R', 'P', 'S'};

void init()
{
	for (int i = 0; i <= n; i++)
	{
		for (int value = 0; value < 3; value++)
		{
			if (i == 0)
			{
				str[i][value] = "";
				str[i][value].push_back(REPR[value]);

				vector <int> arr = {0, 0, 0};
				arr[value] = 1;
				produce[i][value] = arr;
			}
			else
			{
				str[i][value] = min(str[i - 1][value], str[i - 1][(value + 1) % 3]) + max(str[i - 1][value], str[i - 1][(value + 1) % 3]);
				produce[i][value] = produce[i - 1][value];
				for (int s = 0; s < 3; s++)
					produce[i][value][s] += produce[i - 1][(value + 1) % 3][s];
			}
		}
	}
}

void solve()
{
	init();
	for (int i = 0; i < 3; i++)
	{
		if (produce[n][i][0] == R && produce[n][i][1] == P && produce[n][i][2] == S)
		{
			cout << str[n][i] << endl;
			return;
		}
	}
	puts("IMPOSSIBLE");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
