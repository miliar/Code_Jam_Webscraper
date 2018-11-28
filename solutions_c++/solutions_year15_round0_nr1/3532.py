#include <bits/stdc++.h>
using namespace std;

int test;
int a[1111];
int n;
string s;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> n;
		cin >> s;
		for(int i = 0; i < s.length(); i++)
			a[i] = s[i] - '0';
		int s = a[0];
		int k = 0;
		for(int i = 1; i <= n; i++)
		{
			if(s >= i) s += a[i];
			else
			{
				s++;
				k++;
				s += a[i];
			}
		}
		cout << k << "\n";
	}
	return 0;
}