#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int a[4][4],b[4][4];
int main()
{
	int t,i,j,cnt,f,s,tc=1,x;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("o.txt","w",stdout);
	scanf("%d",&t);
	while(tc<=t)
	{
		scanf("%d",&f);
		f--;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		}
		scanf("%d",&s);
		s--;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		}
		cnt=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[f][i]==b[s][j])
				{
					x=a[f][i];
					cnt++;
					break;
				}
			}
		}
		printf("Case #%d: ",tc);
		if(cnt==0)
			printf("Volunteer cheated!\n");
		else if(cnt==1)
			printf("%d\n",x);
		else
			printf("Bad magician!\n");
		tc++;
	}
	fclose(stdin);
	fclose(stdout);
}
