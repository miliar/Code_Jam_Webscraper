#include<cstdio>
#include<cstring>
#include<math.h>
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;
char buf[10086];
int S[10086];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,P=0;
	scanf("%d",&T);
	while(T--)
	{
		int Smax;
		scanf("%d",&Smax);
		scanf("%s",buf);
		S[0]=buf[0]-'0';
		for(int i=1;i<=Smax;i++)S[i]=S[i-1]+buf[i]-'0';
		int ans=0;
		for(int i=1;i<=Smax;i++)
		{
			ans+=fmax(0,i-S[i-1]-ans);
		}
		printf("Case #%d: %d\n",++P,ans);
	}
	return 0;
}

