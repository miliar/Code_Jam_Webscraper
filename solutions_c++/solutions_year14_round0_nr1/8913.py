#include<cstdio>

int main()
{
int i,j,k,l,m,n,t;
int ans[4];
int ans2[4];

scanf("%d",&t);
for(m=1;m<=t;m++)
	{
	scanf("%d",&l);

	for(j=0;j<4;j++)
		{
		if(j==l-1)
			scanf("%d%d%d%d",&ans[0],&ans[1],&ans[2],&ans[3]);
		else
			scanf("%d%d%d%d",&k,&k,&k,&k);
		}

	scanf("%d",&l);

	for(j=0;j<4;j++)
		{
		if(j==l-1)
			scanf("%d%d%d%d",&ans2[0],&ans2[1],&ans2[2],&ans2[3]);
		else
			scanf("%d%d%d%d",&k,&k,&k,&k);
		}
	for(i=0;i<4;i++)
		{
		for(j=0;j<4;j++)
			{
	//		printf("(%d,%d) (%d,%d)\n",i,j,ans[i],ans2[j]);
			if(ans[i]==ans2[j]) break;
			}
		if(j==4) ans[i]=-1;
		}
	k=0;
	for(i=0;i<4;i++)
		if(ans[i]!=-1)
			{
			n=ans[i];
			k++;
			}
	if(k==0)
		printf("Case #%d: Volunteer cheated!\n",m);
	else if(k==1)
		printf("Case #%d: %d\n",m,n);
	else
		printf("Case #%d: Bad magician!\n",m);

	}

return 0;
}
