#include <bits/stdc++.h>

using namespace std;

#define bug() printf("BUG\n")
#define bug1(n) printf("bg1 %d\n",n)
#define bug2(a,b) printf("bg2 %d %d\n",a,b)
#define MOD 1000000007
#define ll long long
#define vi vector< int >
#define vll vector< long long >
#define vvi vector< vector< int > >
#define vvll vector< vector< long long > >
#define pi pair< int, int >
#define pll pair< long long, long long >
#define vpi vector< pair< int, int > >
#define vpll vector< pair< long long, long long > >
#define pb(n) push_back(n)
#define mp(a,b) make_pair(a,b)
#define printA(a,n) for(int i = 0;i < n;++i) cout<<a[i]<<" "; cout<<endl;

int AllP(string s,int len)
{
	for (int i = 0; i < len; ++i)
	{
		if(s[i] == '-')
			return 0;
	}
	return 1;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int tc = 1; tc <= t; ++tc)
	{
		string s;
		cin>>s;
		int len = s.length();
		int ans = 0;
		while(1)
		{
			if(AllP(s,len))
			{
				break;
			}
			if(s[0] == '+')
			{
				ans++;
				for (int i = 0; i < len; ++i)
				{
					if (s[i] == '+')
						s[i] = '-';
					else
						break;
				}
			}
			else
			{
				ans++;
				int last,t1,t2;
				for (int i = 0; i < len; ++i)
				{
					if(s[i] == '-')
						last = i;
				}
				int j = 0,k = last;
				for (int i = 0; i <= last; ++i)
				{
					if (j == k)
					{
						if(s[i] == '+')
							s[i] = '-';
						else
							s[i] = '+';
						break;
					}
					if (k < j)
						break;
					if (s[j] == '+')
						t1 = 0;
					else
						t1 = 1;
					if(s[k] == '-')
						t2 = 1;
					else
						t2 = 0;
					if(t1 == 1)
						s[k] = '+';
					else
						s[k] = '-';
					if(t2 == 1)
						s[j] = '+';
					else
						s[j] = '-';
					++j;
					--k;
				}
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}