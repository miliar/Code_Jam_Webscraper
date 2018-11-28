#include<bits/stdc++.h>
using namespace std;
#define for1(i,n) for(i=0;i<n;i++)
#define for2(i,n) for(i=n-1;i>=0;i--)
#define ll long long int
#define CLEAR(array, value) memset(array, value, sizeof(array));
#define si(a)     scanf("%d", &a)
#define sl(a)     scanf("%lld", &a)
#define sc(a)     scanf(" %c", &a)
#define ss(a)     scanf("%s", a)
#define pi(a)     printf("%d\n", a)
#define pl(a)     printf("%lld\n", a)
#define pn        printf("\n")
 
#define mod long(1e9+7)

int	main() 
{			
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	ll t,j,k;
	sl(t);
	for(j=1;j<=t;j++)
	{
		ll i;
		char s[10000],b[10000];
		ss(s);
		std::list<char> ans;
		ans.push_back(s[0]);
		for(i=1;i<strlen(s);i++)
		{
			char c=ans.front();
			char d=ans.back();
			if(s[i]>=c)
			{
				ans.push_front(s[i]);
			}
			else
			{
				ans.push_back(s[i]);
				
			}
		}
		printf("Case #%lld: ",j);
		while (!ans.empty())
		  {
		    printf("%c",ans.front());
		    ans.pop_front();
		  }
		  pn;
	}	
	return 0;
}

