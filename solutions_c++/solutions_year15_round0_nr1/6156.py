#include <bits/stdc++.h>

#define ll long long
#define __(x) cout << #x << " : " << x << endl;
#define out(a, i, n) for (int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < n; i++)

#define INOUT
//#define TIME	

using namespace std;

int a[1111];

void print(int test, int ans)
{
	printf("Case #%d: %d\n", test, ans);
}

int main()
{
#ifdef INOUT
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		int n; char ch;
		cin >> n;
		forn(i, n+1)
		{
			cin >> ch;
			a[i] = ch - '0';
		}
		int ans = 0, men = a[0];
		for (int i = 1; i < n + 1; i++)
		{
			if (i - men > 0)
			{
				ans += i - men;
				men += i - men;
			}
			men += a[i];
		}
		print(test, ans);
	}

#ifdef TIME
	cout << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
