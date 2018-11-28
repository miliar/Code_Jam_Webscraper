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

int main()
{
	int t;
	scanf("%d",&t);
	for(int tc = 1; tc <= t; ++tc)
	{
		int n;
		scanf("%d",&n);
		int a[10] = {0};
		int cnty = 0;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n",tc);
			continue;
		}
		int temp = n,t1 = n;
		for (int i = 1; i <= 1000; ++i)
		{
			while(temp > 0)
			{
				if (a[temp%10] == 0)
				{
					a[temp%10] = 1;
					cnty++;
				}
				temp/=10;
			}
			if (cnty == 10)
			{
				break;
			}
			n+=t1;
			temp=n;
		}
		if (cnty == 10)
		{
			printf("Case #%d: %d\n", tc,n);
		}
		else
			printf("Case #%d: INSOMNIA\n", tc);
	}
	return 0;
}