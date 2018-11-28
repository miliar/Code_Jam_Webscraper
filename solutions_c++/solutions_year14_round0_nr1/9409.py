#include<cstdio>
#include<cstring>
int a[5][5],b[5][5],aa,bb;
int hash[69];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tt=1;tt<=test;tt++)
	{
		printf("Case #%d: ",tt);
		scanf("%d",&aa);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)scanf("%d",&a[i][j]);
		scanf("%d",&bb);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)scanf("%d",&b[i][j]);
		memset(hash,0,sizeof(hash));
		for(int j=1;j<=4;j++)hash[a[aa][j]]++;
		for(int j=1;j<=4;j++)hash[b[bb][j]]++;
		int ans=0;
		for(int i=1;i<=16;i++)
			if(hash[i]==2)
				if(ans==0)ans=i;
				else ans=69;
		if(ans==0)printf("Volunteer cheated!\n");
		else if(ans==69)printf("Bad magician!\n");
		else printf("%d\n",ans);
	}
	return 0;
}
