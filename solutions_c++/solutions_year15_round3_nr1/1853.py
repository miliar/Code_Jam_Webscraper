#include <cstdio>
#include <algorithm>

using namespace std;
 
int T,r,c,w;
int s[29],p;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out ","w",stdout);
	scanf("%d",&T);
	for (int _=1;_<=T;++_)
	{
		scanf("%d%d%d",&r,&c,&w);
		int ans=0;
		if (w==1)
		{
			ans=r*c;
		}
		else
		{
			p=0;
			for (int i=1;i<=c;++i)
			{
				if (i%w==0) s[p++]=i;
			}
			ans=0X7FFFFFFF;
			do
			{
				int tmp=0;
				for (int i=0;i<p;++i)
				{
					int k=i+1;
					if (s[i]>1 && s[i]<c) k+=w;
					else k+=w-1;
					tmp=max(tmp,k);
				}
				ans=min(ans,tmp);
			}
			while (next_permutation(s,s+p));
			ans*=r;
		}
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
