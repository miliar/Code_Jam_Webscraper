#include<stdio.h>

int main()
{
	int t,l=0;
	scanf("%d",&t);
	while(t--)
	{
		l++;
		int n1,n2,cnt=0,i,j,a[6][6],b[6][6],f[20],p;
		scanf("%d",&n1);
		
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		scanf("%d",&a[i][j]);
		
		scanf("%d",&n2);
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		scanf("%d",&b[i][j]);
		
		for(i=0;i<20;i++)
		f[i]=0;
		
		for(i=1;i<=4;i++)
		f[a[n1][i]]=1;
		
	//	for(i=0;i<20;i++)
	//	printf("%d  \n",f[i]);
	//	printf("\n");
		
		for(i=1;i<=4;i++)
		if(f[b[n2][i]]==1)
		{
			cnt++;
			 p=b[n2][i];
	//		 printf("%d\n",p);
		}
	//	printf("%lld\n",cnt);
		if(cnt==1)
		printf("Case #%d: %d\n",l,p);
		else if(cnt==0)
		printf("Case #%d: Volunteer cheated!\n",l);
		else
		printf("Case #%d: Bad magician!\n",l);
	}
	return 0;
}
