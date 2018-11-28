#include<iostream>
using namespace std;
int rec1[4][4];
int rec2[4][4];
int main()
{
	freopen("F://ini.txt","r",stdin);
	freopen("D://out.txt", "w", stdout);

	int n;
	int k=0;
	scanf("%d",&n);
	while(k++<n)
	{
		int a1,a2;
		int flag=0,ans=0;
		int mp[17];
		memset(mp,0,sizeof(mp));
		scanf("%d",&a1);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&rec1[i][j]);
		for(int i=0;i<4;i++)
			mp[rec1[a1-1][i]]=1;
		scanf("%d",&a2);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&rec2[i][j]);
		for(int i=0;i<4;i++)
		mp[rec1[a1-1][i]]++;
		for(int i=1;i<=16;i++)
			if(mp[i]==2&&flag==0)
			{
				ans=mp[i];
				flag++;
			}
			else if(mp[i]==2&&flag==1)
			{
				flag++;
				break;
			}
		if(flag==1)
			printf("Case #%d: %d\n",k,ans);
		else if(flag==0)
			printf("Case #%d: Volunteer cheated!\n",k);	
		else
			printf("Case #%d: Bad magician!\n",k);
	}
	
	return 0;
}