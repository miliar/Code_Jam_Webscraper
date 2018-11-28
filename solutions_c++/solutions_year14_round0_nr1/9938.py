#include<iostream>
#include<cstdio>

int main()
{
	int a[5][5],b[5][5],m,n,t,i,j,k=1;
	scanf("%d",&t);
	while(t--)
	{
		int res=0,ct=0;
		scanf("%d",&m);
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&n);
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
				scanf("%d",&b[i][j]);		
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
			{
				if(a[m][i]==b[n][j])
				{
					res=a[m][i];
					ct++;
				}
			}

		if(ct == 1)
			printf("Case #%d: %d\n",k++,res);
		else if(ct > 1)
			printf("Case #%d: Bad magician!\n",k++);
		else if (ct==0)
			printf("Case #%d: Volunteer cheated!\n",k++);
	}
	return 0;
}