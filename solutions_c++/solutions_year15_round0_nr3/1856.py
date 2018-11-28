#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

const int N = 10004;
char s[N];
char m[N][N];

#define I 2
#define J 3
#define K 4

int table[5][5] = {
	/*-*/{ 0, 0, 0, 0, 0 },
	/*1*/{ 0, 1, I, J, K },
	/*i*/{ 0, I, -1, K, -J },
	/*j*/{ 0, J, -K, -1, I },
	/*k*/{ 0, K, J, -I, -1 },
};

int mul(int a, int b)
{
	int sg = 1;
	if (a * b < 0)
		sg = -1;
	int res = table[abs(a)][abs(b)];
	return res * sg;
}

void Solution()
{
	int n, rep;
	cin >> n >> rep;
	cin >> s;

	for (int i = 1; i < rep; i++)
		for (int j = 0; j < n; j++)
			s[i * n + j] = s[j];

	n *= rep;
	for (int i = 0; i < n; i++)
	{
		if (s[i] == 'i')
			s[i] = I;
		if (s[i] == 'j')
			s[i] = J;
		if (s[i] == 'k')
			s[i] = K;
	}


	for (int i = 0; i < n; i++)
	{
		m[i][i] = s[i];
		for (int j = i + 1; j < n; j++)
			m[i][j] = mul(m[i][j - 1], s[j]);
	}

	for (int i = 1; i < n; i++)
		for (int j = i + 1; j < n; j++)
		{
			int ii = m[0][i - 1];
			int jj = m[i][j - 1];
			int kk = m[j][n - 1];
			if (ii == I && jj == J && kk == K)
			{
				cout << "YES";
				return;
			}
		}

	cout << "NO";
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}