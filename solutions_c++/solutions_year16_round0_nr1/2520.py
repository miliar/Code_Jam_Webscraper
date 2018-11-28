#include <bits/stdc++.h>

#define ll long long
#define __(x) cout << #x << " : " << x << endl;
#define out(a, i, n) for (int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < n; i++)

#define INOUT
#define TIME	

using namespace std;

void print(int test, int ans)
{
	cout << "Case #" << test << ": " << ans << endl;
	//printf("Case #%d: %d\n", test, ans);
}

void print(int test, string ans)
{
	cout << "Case #" << test << ": " << ans << endl;
}

void gen()
{
	freopen("input.txt", "w", stdout);
	cout << 1000000 << endl;
	for (int i = 0; i < 1000000; i++)
	{
		cout << i << endl;
	}
}

int main()
{
	//gen(); return 0;
#ifdef INOUT
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int tests;
	cin >> tests;
	ll ans = 0;
	for (int test = 1; test <= tests; test++)
	{
		ll n;
		cin >> n;
		set <int> s;
		int step = 1;
		while (s.size() != 10 && step <= 100)
		{
			ll nn = n * step;
			while (nn)
			{
				s.insert(nn % 10);
				nn /= 10;
			}
			step++;
		}
		step--;
		if (s.size() == 10)
		{
			print(test, n * step);
		}
		else
		{
			print(test, "INSOMNIA");
		}
	}

#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
