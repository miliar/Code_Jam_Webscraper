#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define FILE "test"

void out(int ans)
{
	if (ans == -1)
	{
		printf("INSOMNIA\n");
	}
	else
	{
		printf("%d\n", ans);
	}
}

int main()
{
  freopen(FILE".in", "r", stdin);
  freopen(FILE".out", "w", stdout);
  srand(time(0));
	int t;
	cin >> t;
	int Case = 0;
	while (t--)
	{
		string s;
		cin >> s;
		s += '#';
		printf("Case #%d: ", (++Case));
		int ans1 = 0;
		int ans2 = 1;
		int cur = 0;
		char ch;
		//ans1
		ch = s[0];
		vector < int > a1;
		for (int i = 0; i < s.length(); i++)
			if (s[i] == ch)
				cur++;
			else
				a1.push_back(cur), cur = 0, ch = s[i];
		ch = s[0];
		for (int i = 0; i < a1.size(); i++){
			if (ch == '-'){
				ans1 += 1;
			}
			else{
				if (i != a1.size() - 1)
					ans1 += 1;
			}
			ch = (ch == '-' ? '+' : '-');
		}
		//rev
		for (int i = 0; i < s.length() - 1; i++){
			s[i] = (s[i] == '-' ? '+' : '-');
		}
		//
		ch = s[0];
		vector < int > a2;
		for (int i = 0; i < s.length(); i++)
			if (s[i] == ch)
				cur++;
			else
				a2.push_back(cur), cur = 0, ch = s[i];
		ch = s[0];
		for (int i = 0; i < a2.size(); i++){
			if (ch == '-'){
				ans2 += 1;
			}
			else{
				if (i != a2.size() - 1)
					ans2 += 1;
			}
			ch = (ch == '-' ? '+' : '-');
		}
		//
		cerr << ans1 << " " << ans2 << endl;
		out(min(ans1, ans2));
	}
}
