#include<bits/stdc++.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",&a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define rep(i)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long
char s[110];
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	int t,n,i;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		ss(s);
		n=strlen(s);
		int ans=0;
		for(i=n-1;s[i]=='+';--i);
		if(i>=0)
			ans++;
		--i;
		for(;i>=0;--i)
			if(s[i]!=s[i+1])
				ans++;
		printf("Case #%d: %d\n",tt,ans);
	}
}