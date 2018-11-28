#include<bits/stdc++.h>
#define LL long long int
#define REP(i,n) for(int i=0;i<n;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define TC int t;scanf("%d",&t);while (t-->0)
#define INP(x) scanf("%d",&x)
#define OUT(x) printf("%d\n",x)
#define INPLL(x) scanf("%lld",&x)
#define OUTLL(x) printf("%lld\n",x)
#define INPS(x) scanf("%s",x)
#define MEM(a,b) memset(a,b,sizeof(a))
#define MP make_pair
#define PB push_back
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define VPII vector<pair<int,int >
#define F first
#define S second
#define MOD 1000000007
#define mod 10000007
using namespace std;
int main()
{
	int t,l;
	char s[105];
	INP(t);
	for(int xx=1;xx<=t;xx++)
	{
		INPS(s);
		l=strlen(s);
		int i=l-1,cnt=0,j;
		while(i>-1)
		{
			//cout<<s<<endl;
			if(s[i]=='+')
				i--;
			else
			{
				cnt++;
				while(s[i]=='-')
				{
					s[i]='+';
					i--;
				}
				j=i;
				while(j>=0)
				{
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
					j--;
				}
			}
		}
		printf("Case #%d: %d\n",xx,cnt);
	}
	return 0;
}