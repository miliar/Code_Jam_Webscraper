#include <stdio.h>
#include <string.h>

int nrcif[110];
int cate[55][7000][110];
int st[110], dr[110];
char s[250];

void mul (int a[], int b[])
{
	int c[110] = {0}, i, j, t;
	
	for (i = 1; i <= a[0]; i ++)
	{
		for (t = 0, j = 1; j <= b[0] || t; j ++, t /= 10)
			c[i + j - 1] = (t += c[i + j - 1] + a[i] * b[j] ) % 10;
		if (i + j - 2 > c[0])
			c[0] = i + j - 2;
	}
	memcpy (a, c, sizeof (c));
}

void verif (int poz, int v[], int cif)
{
	int a[110] = {0}, i;
	for (i = 1; i <= v[0] / 2; i ++)
		a[++ a[0]] = v[i];
	a[++ a[0]] = cif;
	if (poz % 2 == 0)
		a[++ a[0]] = cif;
	for (; i <= v[0]; i ++)
		a[++ a[0]] = v[i];
	
	mul (a, a);
	int st = 1, dr = a[0];
	while (st <= dr)
	{
		if (a[st] != a[dr])
			return;
		st ++;
		dr --;
	}
	
	nrcif[poz] ++;
	for (i = 1; i <= v[0] / 2; i ++)
		cate[poz][nrcif[poz]][++ cate[poz][nrcif[poz]][0]] = v[i];
	cate[poz][nrcif[poz]][++ cate[poz][nrcif[poz]][0]] = cif;
	if (poz % 2 == 0)
		cate[poz][nrcif[poz]][++ cate[poz][nrcif[poz]][0]] = cif;
	for (; i <= v[0]; i ++)
		cate[poz][nrcif[poz]][++ cate[poz][nrcif[poz]][0]] = v[i];

}

void precalc ()
{
	nrcif[1] = 3;
	cate[1][1][0] = cate[1][2][0] = cate[1][3][0] = 1;
	cate[1][1][1] = 1;
	cate[1][2][1] = 2;
	cate[1][3][1] = 3;
	nrcif[2] = 2;
	cate[2][1][0] = cate[2][2][0] = 2;
	cate[2][1][1] = cate[2][1][2] = 1;
	cate[2][2][1] = cate[2][2][2] = 2;
	
	int i, j;
	for (i = 3; i <= 51; i ++)
		if (i & 1)
		{
			for (j = 1; j <= nrcif[i - 1]; j ++)
			{
				verif (i, cate[i - 1][j], 0);
				verif (i, cate[i - 1][j], 1);
				verif (i, cate[i - 1][j], 2);
			}
		}
		else
		{
			for (j = 1; j <= nrcif[i - 2]; j ++)
			{
				verif (i, cate[i - 2][j], 0);
				verif (i, cate[i - 2][j], 1);
			}
		}
}

int cmp (int a[], int b[])
{
	int i;
	for (i = 1; i <= a[0]; i ++)
		if (a[i] != b[i])
			return a[i] > b[i];
	return 0;
}

int rez (int v[])
{
	int i, sol = 0;
	for (i = 1; i < v[0]; i ++)
		sol += nrcif[i];
	for (i = 1; i <= nrcif[v[0]]; i ++)
		if (cmp (cate[(v[0] + 1) / 2][i], v))
			return sol;
		else
			sol ++;
	return sol;
}

int main ()
{
	freopen ("input.in", "r", stdin);
	freopen ("output.out", "w", stdout);
	
	precalc ();
	
	int i, j, k;
	for (i = 1; i <= 51; i ++)
	{
		for (j = 1; j <= nrcif[i]; j ++)
		{
			mul (cate[i][j], cate[i][j]);
//			for (k = 1; k <= cate[i][j][0]; k ++)
//				printf ("%d", cate[i][j][k]);
//			printf ("\n");
		}
	}
	for (i = 105; i >= 1; i --)
		if (i & 1)
			nrcif[i] = nrcif[(i + 1) / 2];
		else
			nrcif[i] = 0;
	int tt, t, sol;
	scanf ("%d\n", &tt);
	for (t = 1; t <= tt; t ++)
	{
		sol = 0;
		memset (s, 0, sizeof (s));
		memset (st, 0, sizeof (st));
		memset (dr, 0, sizeof (dr));
		gets (s + 1);
		
		for (i = 1; s[i] != ' '; i ++)
			st[++ st[0]] = s[i] - '0';
		if (st[st[0]] != 0)
			st[st[0]] --;
		i ++;
		for (; '0' <= s[i] && s[i] <= '9'; i ++)
			dr[++ dr[0]] = s[i] - '0';
		
		printf ("Case #%d: %d\n", t, rez (dr) - rez (st));
	}
	return 0;
}
