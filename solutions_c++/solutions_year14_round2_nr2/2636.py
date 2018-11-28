#include<stdio.h>
int main()
{
	freopen("C:\\Users\\manish\\Desktop\\input.txt","r",stdin);
 	freopen("C:\\Users\\manish\\Desktop\\output.txt","w",stdout);
	int t,i,j,k,l,a,b;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{int c=0;
		int a,b,k;
		scanf("%d%d%d",&a,&b,&k);
		for(j=0;j<a;j++)
		{
			for(l=0;l<b;l++)
				{
					if((j&l)<k)
						c++;
				}
		}
		printf("Case #%d: %d\n",i,c);
	}
	return 0;
}
