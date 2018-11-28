#include<cstdio>
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int A[]={1,4,9,121,484};
	int T,l,u;
	scanf("%d",&T);
	int i=0;
	while(T--)
	{
		int c=0;
		i++;
		scanf("%d %d",&l,&u);
		for(int j=l;j<=u;j++)
		{
			for(int k=0;k<5;k++)
			{
				if(j==A[k])
					c+=1;
			}
		}
							printf("Case #%d: %d\n",i,c);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
