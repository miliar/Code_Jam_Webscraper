#include <stdio.h>
#include <string.h>

//int arr[4][4];
int c[17];

int main()
{
	//freopen("in.in","r",stdin);

	int T,temp,ans,flag,time=0;
	scanf("%d",&T);

	while(T--)
	{
		flag=true;
		ans=-1;
		memset(c,0,sizeof(c));
		int r1,r2;
		scanf("%d",&r1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&temp);
				if( i+1==r1) c[temp]++;
			}
		}
		scanf("%d",&r2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&temp);
				if( i+1==r2 ) c[temp]++;
			}
		}

		for(int i=1;i<=16;i++)
		{
			if( c[i]==2){
				if(!flag) {
					ans=-2;
					break;
				}
				ans=i;
				flag=false;
			}
		}

		if( ans==-1 ) printf("Case #%d: Volunteer cheated!\n",++time);
		else if( ans==-2 ) printf("Case #%d: Bad magician!\n",++time);
		else printf("Case #%d: %d\n",++time,ans);

	}

		
	return 0;
}