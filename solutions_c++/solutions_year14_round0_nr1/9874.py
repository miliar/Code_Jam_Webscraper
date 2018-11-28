#include<stdio.h>
int a[7][7],b[7][7];
int main()
{
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A.out","w",stdout);
	int N,first=1,t;
	scanf("%d",&N);
	while(N--)
	{
		int n,m,i,j,s=0;
		scanf("%d",&n);
		n--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		m--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(a[n][i]==b[m][j])
				{
					t=a[n][i];
					s++;
				}
		if(s==0)
			printf("Case #%d: Volunteer cheated!\n",first++);
		else if(s>1)
			printf("Case #%d: Bad magician!\n",first++);
		else
			printf("Case #%d: %d\n",first++,t);
	}
	return 0;
}