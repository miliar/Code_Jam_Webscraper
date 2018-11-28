#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
	int T;
	int cnt;
	int i,j,l;
	int ans1;
	int ans2;
	int map1[5][5],map2[5][5];
	//freopen("C:\\Users\\lovesunmoon\\Desktop\\Problem 1in.txt","r",stdin);
   	//freopen("C:\\Users\\lovesunmoon\\Desktop\\Problem 1out.txt","w",stdout);
	scanf("%d",&T);
	for(cnt=1;cnt<=T;cnt++)
	{
		scanf("%d",&ans1);
		memset(map1,0,sizeof(int));
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		scanf("%d",&map1[i][j]);
		int temp1[5];
		memset(temp1,0,sizeof(int));
		for(j=1;j<=4;j++)
		temp1[j]=map1[ans1][j];
		memset(map2,0,sizeof(int));
		scanf("%d",&ans2);
		for(i=1;i<5;i++)
		for(j=1;j<5;j++)
		scanf("%d",&map2[i][j]);
		int temp2[5];
		memset(temp2,0,sizeof(int));
		for(j=1;j<=4;j++)
		temp2[j]=map2[ans2][j];
		int ans=0;
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		{
			if(temp1[i]==temp2[j])
			ans++;
		}
		printf("Case #%d: ",cnt);
		if(ans==0)
		printf("Volunteer cheated!\n");
		else if(ans==1)
		{
			for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			if(temp1[i]==temp2[j])
			{printf("%d\n",temp1[i]);
			break;}
		}
		else
		printf("Bad magician!\n");
	}
}