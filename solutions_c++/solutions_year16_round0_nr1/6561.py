#include "iostream"
#include "cstdio"
#include "cstring"

using namespace std;

int N, T, a[100], c[100];
bool vis[11];

int f(int n)
{
	int m = 0;
	for(int i = 10; i/10 <= n; i *= 10)
		a[m++] = (n%i)/(i/10);
	return m;
}

int mults(int *a, int na, int *c, int b)
{
	int i, s, carry = 0;
	for(i = 0; i < na; i++)
	{
		s = carry + a[i]*b;
		c[i] = s % 10;
		carry = s / 10;
	}
	while(carry)
	{
		c[na] = carry % 10;
		carry = carry / 10;
		na++;
	}
	return na;
}

int main()
{
	// freopen("data.in", "r", stdin);
	// freopen("data.out", "w", stdout);
	int cnt = 0;
	cin >> T;
	while(T--)
	{
		memset(vis, 0, sizeof(vis));
		cnt++;
		cin >> N;

		if(N == 0)
		{
			cout << "Case #" << cnt << ": INSOMNIA" << endl;
			continue;
		}

		int k = 0, na = f(N), nc;
		bool flag = true;
		while(flag)
		{
			k++;
			nc = mults(a, na, c, k);

			// for(int i = nc-1; i >= 0; i--)
			// 	cout << c[i];
			// cout << endl;

			flag = false;
			for(int i = 0; i < nc; i++)
				vis[c[i]] = 1;
			for(int i = 0; i <= 9; i++)
				if(!vis[i])
				{
					flag = true;
					break;
				}
		}

		cout << "Case #" << cnt << ": ";
		for(int i = nc-1; i >= 0; i--)
			cout << c[i];
		cout << endl;
	}
	return 0;
}