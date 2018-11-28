#include <bits/stdc++.h>

using namespace std;

char p[3][20][5123];
char pf[3][20][5123];
char pf2[3][20][5123];
int c[3][20][3];

int main()
{
	//type = PRS
	//type, level, char
	p[0][0][0] = 'P';
	p[1][0][0] = 'R';
	p[2][0][0] = 'S';
	pf[0][0][0] = 'P';
	pf[1][0][0] = 'R';
	pf[2][0][0] = 'S';
	pf2[0][0][0] = 'P';
	pf2[1][0][0] = 'R';
	pf2[2][0][0] = 'S';
	c[0][0][0] = 1;
	c[1][0][1] = 1;
	c[2][0][2] = 1;
	for (int i = 0; i < 12; i++)
	{
		for (int k = 0; k < 3; k++)
		{
			c[k][i+1][0] = c[k][i][0];
			c[k][i+1][1] = c[k][i][1];
			c[k][i+1][2] = c[k][i][2];
			for (int j = 0; j < (1<<i); j++)
			{
				if (p[k][i][j] == 'P')
				{
					p[k][i+1][j*2] = 'P';
					p[k][i+1][j*2+1] = 'R';
					pf2[k][i+1][j*2] = 'P';
					pf2[k][i+1][j*2+1] = 'R';
					c[k][i+1][1]++;
				}
				if (p[k][i][j] == 'R')
				{
					p[k][i+1][j*2] = 'S';
					p[k][i+1][j*2+1] = 'R';
					pf2[k][i+1][j*2] = 'S';
					pf2[k][i+1][j*2+1] = 'R';
					c[k][i+1][2]++;
				}
				if (p[k][i][j] == 'S')
				{
					p[k][i+1][j*2] = 'S';
					p[k][i+1][j*2+1] = 'P';
					pf2[k][i+1][j*2] = 'P';
					pf2[k][i+1][j*2+1] = 'S';
					c[k][i+1][0]++;
				}
				if (pf2[k][i][j] == 'P')
				{
					pf[k][i+1][j*2] = 'P';
					pf[k][i+1][j*2+1] = 'R';
				}
				if (pf2[k][i][j] == 'R')
				{
					pf[k][i+1][j*2] = 'R';
					pf[k][i+1][j*2+1] = 'S';
				}
				if (pf2[k][i][j] == 'S')
				{
					pf[k][i+1][j*2] = 'P';
					pf[k][i+1][j*2+1] = 'S';
				}
			}
		}
	}
	int T;
	cin >> T;
	int n, ps, rs, ss;
	for (int C = 1; C <= T; C++)
	{
		cin >> n >> rs >> ps >> ss;
		char *best = NULL;
		for (int k = 0; k < 3; k++)
		{
			if (c[k][n][0] == ps && c[k][n][1] == rs && c[k][n][2] == ss)
			{
				if (best == NULL) best = pf[k][n];
				else if (lexicographical_compare(pf[k][n], pf[k][n] + (1<<n), best, best + (1<<n))) best = pf[k][n];
			}
		}
		cout << "Case #" << C << ": ";
		if (best == NULL) cout << "IMPOSSIBLE";
		else cout << best;
		cout << '\n';
	}
	return 0;
}

