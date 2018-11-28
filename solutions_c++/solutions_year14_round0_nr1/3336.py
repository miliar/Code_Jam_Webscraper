#include<cstdio>
#include<cstring>

int a[5][5],s[20];

int main()
{
//	freopen("E:/in.txt","r",stdin);
//	freopen("E:/out.txt","w",stdout);
	int T,t,z,n,i,j;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		memset(s,0,sizeof(s));
		for(z=1;z<=2;z++)
		{
			scanf("%d",&n);
			for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
			for(i=1;i<=4;i++)
				s[a[n][i]]++;
		}
		for(z=0,i=1;i<=16;i++)
		if(s[i]==2)
		{
			if(z)
				z=-1;
			else
				z=i;
		}
		if(z>0)
			printf("%d\n",z);
		else
			puts(z?"Bad magician!":"Volunteer cheated!");
	}
	return 0;
}
