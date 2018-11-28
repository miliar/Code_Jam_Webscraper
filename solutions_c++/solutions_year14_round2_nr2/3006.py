#include<stdio.h>

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T,A,B,K;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d %d %d",&A,&B,&K);
		int res=0;
		for(int x=0;x<A;x++)
			for(int y=0;y<B;y++)
				if(int(x&y)<K)
					res++;
		printf("Case #%d: %d\n",i+1,res);
	}
}