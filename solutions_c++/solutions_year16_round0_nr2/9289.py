#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int main()
{
	int t = in();
	int tt = 0;
	while(t--)
	{
		tt++;
		cout << "Case #" << tt << ": ";
		string s;
		cin >> s;
		int n = s.size();
		int las = -1;
		for(int i = 0; i < n; i++)
			if(s[i] == '-')
				las = i;
		int ans = 0;
		for(int i = 0; i <= las; i++)
			if(!i || s[i] != s[i - 1])
				ans++;
		cout << ans << endl;
	}
}
