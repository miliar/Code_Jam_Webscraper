#include <bits/stdc++.h>

#define For(i, a, b) for(int i=(a); i<(b); ++i)
#define INF 1000000000
#define MP make_pair

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

const int N = (1 << 16);
vector <int> primos;
bool criba[65540];

ll pot[15][35];

int num[35], divi[15];
int n, J, ans = 0;

bool check()
{
	For(k, 2, 11)
	{
		ll x = 0;

		For(i, 0, n)
			x += num[i]*pot[k][i];

		bool ok = false;
		For(i, 0, (int)primos.size())
		{
			if (primos[i] >= x)
				break;

			if (x % primos[i] == 0)
			{
				divi[k] = primos[i];
				ok = true;
				break;
			}
		}

		if (!ok)
			return false;
	}

	return true;
}

void bt(int ind)
{
	//printf("%d %d\n", ans, J);
	if (ans == J)
		return;

	if (ind == n)
	{
		if (check())
		{
			++ans;

			For(i, 0, n)
				printf("%d", num[n-i-1]);

			For(i, 2, 11)
				printf(" %d", divi[i]);
			printf("\n");
		}

		return;
	}

	if (ind > 0 and ind < n-1)
	{
		num[ind] = 0;
		bt(ind+1);
	}


	num[ind] = 1;
	bt(ind+1);

}

int main()
{
	//std::ios_base::sync_with_stdio(false);

	for (ll i = 2; i <= N; ++i)
		if (!criba[i])
		{
			primos.push_back(i);
			for (ll j = i*i; j <= N; j += i)
				criba[j] = true;
		}

	For(i, 2, 11)
	{
		pot[i][0] = 1;
		For(j, 1, 33)
			pot[i][j] = pot[i][j-1] * i;
	}

	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		scanf("%d %d", &n, &J);
		printf("Case #%d:\n", caso++);
		bt(0);
	}

	return 0;
}