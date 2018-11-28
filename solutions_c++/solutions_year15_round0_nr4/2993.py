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

void print(int test, string ans)
{
	cout << "Case #" << test << ": " << ans << endl;
}

int main()
{
#ifdef INOUT
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int x, r, c;
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cin >> x >> r >> c;
		if (c > r) swap(c, r);
		if (x == 1)
		{
			print(test, "GABRIEL");
			continue;
		}
		if (x == 2)
		{
			if ((r * c) & 1)
				print(test, "RICHARD");
			else 
				print(test, "GABRIEL");
		}
		if (x == 3)
		{
			if (r < 3 && c < 3)
			{
				print(test, "RICHARD");
			}
			else 
			{
				if (r == 3)
				{
					if (c == 1)
						print(test, "RICHARD");
					else 
						print(test, "GABRIEL");
				}
				else 
				{
					if (c < 3 || c == 4)
						print(test, "RICHARD");
					else 
						print(test, "GABRIEL");
				}
			}
		}
		if (x == 4)
		{
			if (r < 4)
				print(test, "RICHARD");
			else 
			{
				if (c < 3)
					print(test, "RICHARD");
				else 
					print(test, "GABRIEL");
			}
		}
	}

#ifdef TIME
	cout << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
