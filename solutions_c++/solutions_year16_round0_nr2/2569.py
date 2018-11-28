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

int main()
{
#ifdef INOUT
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int tests;
	cin >> tests;
	ll ans = 0;
	for (int test = 1; test <= tests; test++)
	{
		string s;
		cin >> s;
		int ans = 0;
		while (true)
		{
			int pos = s.length() - 1;
			while (pos >= 0 && s[pos] == '+') pos--;
			if (pos < 0)
				break;
			while (s[pos] == '-')
			{
				s[pos--] = '+';		
			}
			for (int i = 0; i <= pos; i++)
			{
				s[i] = (s[i] == '-' ? '+' : '-');
			}
			ans++;
		}
		print(test, ans);
	}

#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
