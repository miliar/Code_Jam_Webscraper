#include <stdio.h>


typedef long long ll;

#define pN (8)


int Pr[] = {2,3,5,7,11,13,17,19};
ll baseMod[pN+1][11][50];
ll res[510][20];


void binaryPrint(ll n, ll x){
	ll i;
	for (i = n-1; i >= 0; i--)
	{
		printf ("%d", (x>>i)&1);
	}
}


void fun(ll n, ll J)
{
	ll pi, base, i, j, k;
	ll tot, num, fact, sum;
	for (pi = 0; pi < pN; pi++)
	{
		for (i = 2; i <= 10; i++)
		{
			base = 1;
			for (j = 0; j < n; j++)
				baseMod[pi][i][j] = base,
				base = (base * i) % Pr[pi];
		}
	}
	tot = 0;
	for (num = (1LL<<(n-1)) + 1; num <(1LL <<(n)) && tot < J; num += 2)
	{
		for(i = 2; i <= 10; i++)
		{
			fact = -1;
			for (j = 0; j < pN; j++)
			{
				sum = 0;
				for (k = 0; k < n; k++) if (num & (1LL<<k))
				{
					sum += baseMod[j][i][k];
					sum %= Pr[j];
				}
				if (sum == 0)
				{
					fact = Pr[j];
					break;
				}
			}
			if (fact != -1)
				res[tot][i] = fact;
			else
				break;
		}
		if (i > 10) res[tot++][0] = num;
	}
	for (i = 0; i < tot; i++)
	{
		binaryPrint(n, res[i][0]);
		for (j = 2; j <= 10; j++)
			printf (" %I64d", res[i][j]);
		printf ("\n");
	}
}


int main()
{
	int T, c;
	int n, j;
	freopen ("C-large.in", "r", stdin);
	freopen ("c-large-out.txt", "w", stdout);
	scanf ("%d", &T);
	for (c = 1; c <= T; c++)
	{
		scanf ("%d%d", &n, &j);
		printf ("Case #%d:\n", c);
		fun(n, j);
	}
	return 0;
}
