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
		freopen("A-large.in","r",stdin);
		freopen("A-large.out","w",stdout);
		int t;
		cin >> t;
		int cnt = 1;
		while(t--)
		{
			int n,cur = 0,mn = 0;
			cin >> n;
			for(int i = 0;i <= 9;i ++)
			a[i] = 0;
			for(int i = 1;i <= 1000000;i ++)
			{
				long long p = 1ll * i * 1ll * n;
				while(p)
				{
					int k = p % 10;
					if(!a[k]) cur++;
					a[k] = 1;
					p/= 10;
				}
				if(cur == 10 && !mn)
				{
					mn = 1ll * i * 1ll * n;
				}
			}
			cout << "Case #"<< cnt << ": ";
			if(!mn)
			{
				cout << "INSOMNIA";
			}
			else 
			cout << mn ;
			cout << endl;
			cnt++;
		}
	}

