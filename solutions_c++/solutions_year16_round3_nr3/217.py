// Wsl_F

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>


using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))


int variants[100][5];
int comb[10][5][5];

LL pw[64];

void printAns333(int k)
{
	if (k >= 3)
	{
		cout << 27 << endl;
		cout << "1 1 1" << endl;		cout << "1 1 2" << endl;		cout << "1 1 3" << endl;		cout << "1 2 1" << endl;		cout << "1 2 2" << endl;		cout << "1 2 3" << endl;		cout << "1 3 1" << endl;		cout << "1 3 2" << endl;		cout << "1 3 3" << endl;		cout << "2 1 1" << endl;		cout << "2 1 2" << endl;		cout << "2 1 3" << endl;		cout << "2 2 1" << endl;		cout << "2 2 2" << endl;		cout << "2 2 3" << endl;		cout << "2 3 1" << endl;		cout << "2 3 2" << endl;		cout << "2 3 3" << endl;		cout << "3 1 1" << endl;		cout << "3 1 2" << endl;		cout << "3 1 3" << endl;		cout << "3 2 1" << endl;		cout << "3 2 2" << endl;		cout << "3 2 3" << endl;		cout << "3 3 1" << endl;		cout << "3 3 2" << endl;		cout << "3 3 3" << endl;
		return;
	}

	if (k == 2)
	{
		cout << 18 << endl;
		cout << "1 1 1" << endl;
		cout << "1 1 3" << endl;
		cout << "1 2 1" << endl;
		cout << "1 2 2" << endl;
		cout << "1 3 2" << endl;
		cout << "1 3 3" << endl;
		cout << "2 1 1" << endl;
		cout << "2 1 2" << endl;
		cout << "2 2 2" << endl;
		cout << "2 2 3" << endl;
		cout << "2 3 1" << endl;
		cout << "2 3 3" << endl;
		cout << "3 1 2" << endl;
		cout << "3 1 3" << endl;
		cout << "3 2 1" << endl;
		cout << "3 2 3" << endl;
		cout << "3 3 1" << endl;
		cout << "3 3 2" << endl;

		return;
	}

	cout << 9 << endl;
	cout << "1 1 2" << endl;
	cout << "1 2 1" << endl;
	cout << "1 3 3" << endl;
	cout << "2 1 1" << endl;
	cout << "2 2 3" << endl;
	cout << "2 3 2" << endl;
	cout << "3 1 3" << endl;
	cout << "3 2 2" << endl;
	cout << "3 3 1" << endl;

}


void solve()
{
	int j, p, s, k;
	cin >> j >> p >> s >> k;
	if (j + p + s == 9)
	{
		printAns333(k);
		return;
	}

	int var = 0;
	for (int i = 1; i <= j; i++)
		for (int q = 1; q <= p; q++)
			for (int w = 1; w <= s; w++)
			{
				variants[var][1] = i;
				variants[var][2] = q;
				variants[var][3] = w;
				++var;
			}

	int ansMask = 0;
	int ans = 0;
	for (int mask = 1; mask < pw[var]; mask++)
	{
		int cur = 0;
		for (int i = 0; i < var; i++)
			if ((int)(mask&pw[i]) != 0)
			{
				cur++;
			}
		if (cur <= ans) continue;

		for (int i = 0; i < var; i++)
			if ((int)(mask&pw[i]) != 0)
			{
				bool flag = 1;
				for (int q = 1; q < 3; q++)
					for (int w = q + 1; w <= 3; w++)
					{
						comb[q + w][variants[i][q]][variants[i][w]]++;
						if (comb[q + w][variants[i][q]][variants[i][w]] > k)
						{
							flag = 0;
							break;
						}
					}
				if (!flag)
				{
					cur = 0;
					break;
				}
			}

		if (cur > ans)
		{
			ans = cur;
			ansMask = mask;
		}

		for (int i = 0; i < var; i++)
			if ((int)(mask&pw[i]) != 0)
			{
				for (int q = 1; q < 3; q++)
					for (int w = q + 1; w <= 3; w++)
					{
						comb[q + w][variants[i][q]][variants[i][w]] = 0;
					}
			}

	}

	cout << ans << endl;
	for (int i = 0; i < var; i++)
		if ((int)(ansMask&pw[i]) != 0)
		{
			cout << variants[i][1] << " " << variants[i][2] << " " << variants[i][3] << " " << endl;
		}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	srand(__rdtsc());

	freopen("C-small-attempt0 (1).in", "r", stdin);
	freopen("C-small-output.txt", "w", stdout);
	//cout<<fixed;
	//cout<<setprecision(9);

	pw[0] = 1;
	for (int i = 1; i < 64; i++)
		pw[i] = pw[i - 1] * 2;

	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		cout << "Case #" << testCase << ": ";
		solve();
	}


	return 0;
}
