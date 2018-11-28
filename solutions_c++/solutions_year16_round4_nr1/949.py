#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

const int MAXN = 13;
int T, N, R, P, S;
string A[MAXN];
string ans;

void go(string start)
{
	for (int i = 0; i < MAXN; i++)
		A[i] = "";

	A[0] = start;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < (1 << i); j++)
		{
			if (A[i][j] == 'P')
				A[i + 1] += "PR";
			else if (A[i][j] == 'S')
			{
				if (i == N - 2 || i == N - 1)
					A[i + 1] += "PS";
				else
					A[i + 1] += "SP";
			}
			else
			{
				if (i == N - 1)
					A[i + 1] += "RS";
				else
					A[i + 1] += "SR";
			}
		}
	
	int pcnt = 0, rcnt = 0, scnt = 0;
	for (int i = 0; i < (1 << N); i++)
	{
		if (A[N][i] == 'P')
			pcnt++;
		if (A[N][i] == 'R')
			rcnt++;
		if (A[N][i] == 'S')
			scnt++;
	}

	if ((pcnt == P && rcnt == R && scnt == S) && (ans == "" || ans > A[N]))
		ans = A[N];
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	ios::sync_with_stdio(0);

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> N >> R >> P >> S;
		ans = "";

		go("P");
		go("R");
		go("S");

		if (ans == "")
			cout << "Case #" << t << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << t << ": " << ans << "\n";
	}

	return 0;
}