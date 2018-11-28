 //FUCK

#include<stdio.h>

int t;
int n,m;

int zu[200][200];

int test(int i,int j)
{
	int flag=1;
	for(int k=0;k<n;k++)
	{
		if(zu[k][j]>zu[i][j])
		{
			flag=0;
		}
	}
	if(flag)
	{
		return 1;
	}
	flag=1;
	for(int k=0;k<m;k++)
	{
		if(zu[i][k]>zu[i][j])
		{
			flag=0;
		}
	}
	return flag;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&t);
	for(int tt=0;tt<t;tt++)
	{
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				scanf("%d",&zu[i][j]);
			}
		}

		int flag=1;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				int ran=test(i,j);
				if(!ran)
				{
					flag=0;
				}
			}
		}
		if(flag)
		{
			printf("Case #%d: YES\n",tt+1);
		}
		else
		{
			printf("Case #%d: NO\n",tt+1);
		}
	}
}
