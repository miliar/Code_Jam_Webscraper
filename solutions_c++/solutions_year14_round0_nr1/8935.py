#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	int r,ar[4][4],b[17],t,cnt,x,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		fill(b,b+17,0);
		scanf("%d",&r);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			scanf("%d",&ar[i][j]);
		}
		r--;
		for(int i=0;i<4;i++)
		b[ar[r][i]]=1;
		scanf("%d",&r);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			scanf("%d",&ar[i][j]);
		}
		r--;
		cnt=0;
		for(int i=0;i<4;i++)
		{
			if(b[ar[r][i]]==1)
			{
				cnt++;
				x=ar[r][i];
			}
		}
		printf("Case #%d: ",k);
		if(cnt==1)
		{
			printf("%d\n",x);
		}
		else if(cnt>1)
		{
			printf("Bad magician!\n");
		}
		else
		printf("Volunteer cheated!\n");
	}
	
}
