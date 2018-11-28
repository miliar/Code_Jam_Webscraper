	# include <iostream>
	# include <cstdlib>
	# include <cstdio>
	# include <cmath>
	# include <algorithm>
	# include <set>
	# include <vector>
	# include <map>
	# include <queue>
	# include <stack>
	# include <string>
	# include <cstring>
	# define er erase
	# define pb push_back
	# define pp push
	# define f first
	# define s second
	# define b begin
	# define e end
	
	using namespace std;
	int a[10];
	int main ()
	{
		freopen("B-large.in","r",stdin);
		freopen("B-large.out","w",stdout);
		int t;
		cin >> t;
		int cnt = 1;
		while(t--)
		{
			int cur = 0;
			string s;
			cin >> s;
			for(int i = 1;i < s.size();i ++)
			if(s[i - 1] != s[i]) cur++;
			if(s[s.size() - 1] == '-') cur ++;
			cout << "Case #"<< cnt << ": ";
			cout << cur << endl;
			cnt++;
		}
	}

