#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <string.h>

using namespace std;

string i_to_s(int x)
{
	string s = "";
	while (x)
	{
		s = char(x % 10 + '0') + s;
		x /= 10;
	}
	return s;
}

void get_ans(int x, bool res)
{
	string s = "Case #" + i_to_s(x) + ": ";
	if (res == 1)
		s = s + "YES";
	else
		s = s + "NO";
	cout << s << endl;
}

int T, N, M;
int a[120][120];

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int k = 1; k <= T; ++k)
	{
		scanf("%d %d", &N, &M);
		for (int i = 1; i <= N; ++i)
			a[i][0] = 0;
		for (int i = 1; i <= M; ++i)
			a[0][i] = 0;

		for (int i = 1; i <= N; ++i)
		{
			for (int j = 1; j <= M; ++j)
			{
				scanf("%d", &a[i][j]);
				a[i][0] = max(a[i][0], a[i][j]);
				a[0][j] = max(a[0][j], a[i][j]);
			}
		}

		bool can = true;

		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= M; ++j)
				if (a[i][j] < a[i][0] && a[i][j] < a[0][j])
					can = false;
		get_ans(k, can);
	}
}