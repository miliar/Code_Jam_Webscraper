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
		string s;
		cin >> s;
		string ans = "";
		ans += s[0];
		for (int i = 1; i < s.length(); i++)
		{
			if (ans[0] <= s[i])
			{
				ans = s[i] + ans;
			}
			else 
			{
				ans += s[i];
			}
		}
		print(test, ans);
	}

#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
