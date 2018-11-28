#include <bits/stdc++.h>
using namespace std;

int t, n;
string s;
int a[111];

void invert(int);

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for(int k = 1; k <= t; k++)
	{
		cout << "Case #" << k << ": ";
		cin >> s;
		n = s.length();
		for(int i = 0; i < n; i++)
			if(s[i] == '-') a[i] = 0;
			else a[i] = 1;
		int d = 0;
		int x = n - 1;
		while(x >= 0)
		{
			int y = 0;
			while(y < n && a[y] == 1) y++;
			if(y > 0 && y < n)
			{
				invert(y - 1);
				d++;
			}
			while(x >= 0 && a[x] == 1) x--;
			if(x < 0) break;
			if(x >= 0)
			{
				invert(x);
				d++;
			}
			while(x >= 0 && a[x] == 1) x--;
		}
		cout << d << "\n";
	}
	return 0;
}

void invert(int x)
{
	int b[111];
	for(int i = 0; i <= x; i++)
		b[i] = a[i];
	for(int i = 0; i <= x; i++)
		a[i] = 1 - b[x - i];
}