#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <sstream>
#include <fstream>
#include <functional>
#include <cassert>
#include <complex>
#include <valarray>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long ll;
typedef pair<int, int> pii;
#define X first
#define Y second
#define mp make_pair

string str;
void read()
{
	cin >> str;
}

const int N = (int)1e5 + 10;

char st[N];

void solve()
{
	int r = 0;
	int group = 1;
	for (int i = 1; i <= (int)str.length(); i++)
	{
		if (i < (int)str.length() && str[i] == str[i - 1])
			group++;
		else
		{
			if (group % 2 == 0)
			{
				group = 1;
				continue;
			}
			if (r > 0 && st[r - 1] == str[i - 1])
				r--;
			else
				st[r++] = str[i - 1];
			group = 1;
		}
	}
	int minCnt = 0;
	for (int i = 0; i < r; i++)
	{
		if (st[i] == 'C')
			minCnt++;
	}
	minCnt = min(minCnt, r - minCnt);
	printf("%d\n", 5 * ((int)str.length() - minCnt));
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
