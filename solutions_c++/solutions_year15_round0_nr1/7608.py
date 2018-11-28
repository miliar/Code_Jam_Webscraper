//
// Bhumik Shah
//    IIIT Hyderabad
//
#include <bits/stdc++.h>

#define mod 1000000007
#define f(i,a,b) for(i=a;i<b;i++)
#define ll long long
#define clr(a) memset(a,0,sizeof(a))
#define out(n) cout<<n<<"\n";
#define in(n) cin>>n;

using namespace std;

int main()
{
	int test=0,cnt=0;
	scanf("%d",&test);
	while(cnt!=test)
	{
		long long int ans=0;
		long long int num=0,i=0,no_of_ppl=0;
		string str1;
		scanf("%lld",&num);
		cin>>str1;
		for(i=0;i<=num;i++)
		{
			if(no_of_ppl>=i)
			{
				no_of_ppl+=(long long int)(str1[i]-'0');
			}
			else
			{
				ans+=(long long int)(i-no_of_ppl);
				no_of_ppl+=(i-no_of_ppl);
				no_of_ppl+=(long long int)(str1[i]-'0');
			}
		}
		cnt++;
		printf("Case #%d: %lld\n",cnt,ans);
	}
	return 0;
}
