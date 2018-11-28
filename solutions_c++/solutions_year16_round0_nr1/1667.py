#include <stdio.h>
#include <string.h>
bool mark[10];
int check(long long s)
{
	int ret=0;
	while(s>0)
	{
		if(!mark[s%10]){
			mark[s%10]=true;
			ret++;
		}
		s/=10;
	}
	return ret;
}
int main()
{
	int T,cas=0;
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		
		
		long long  n;
		scanf("%lld",&n);
		printf("Case #%d: ",++cas);
		if(n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		memset(mark,false,sizeof(mark));
		int s=0;
		long long res=n;
		for(int i=0;;i++)
		{
			s+=check(res);
			if(s==10)break;
			res+=n;
		}
		printf("%lld\n",res);
	}
}