#include<bits/stdc++.h>
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define scan(a) scanf("%d",&a)
#define scanl(a) scanf("%lld",&a)
#define print(a) printf("%d",a)
#define printl(a) printf("%lld",a)
#define MAX 10
using namespace std;

typedef pair<int,int>pii;
typedef long long LL;

bool cmp(const pii &left,const pii &right)
{
	return left.second<right.second;
}
int gcd(int a,int b)
{
	if(b==0)
	{
		return a;
	}
	else
		return gcd(b,a%b);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out-large.out","w",stdout);
	int t,z;
	scan(t);
	z=t;
	while(t--)
	{
		int n;
		scan(n);
		string s;
		cin>>s;
		LL sum=0,ans=0;
		if(s[0]=='0')
		{
			sum+=1;
			ans+=1;
		}
		else
		{
			sum+=(s[0]-48);
		}
		for(int i=1;i<=n;i++)
		{
			if((s[i]-48)>0&&sum<i)
			{
				ans+=(i-sum);
				sum=i+(s[i]-48);
			}
			else
			{
				sum+=(s[i]-48);
			}
		}
		printf("Case #%d: %lld\n",z-t,ans);
	}
}
