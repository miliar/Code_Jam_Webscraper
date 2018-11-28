#include<cstdio>
#include<iostream>
#include<cstring> 
#include<vector>
#include<algorithm>
#include<queue>
#include<cmath>
#include<cstdlib>
#define MAXN 100010
#define PI 3.14159265359
#define LEN 0.00001
#define base 100000
#define e 2.71828182846
#define YU 1000000007
#define INF 2147483647
//#define N 50005
using namespace std;
int a[5][5];
int b[5][5];
int flag[20];
int main()
{
	int case_num=0;
	int t,i,j;
	int ans1,ans2,cnt,ans;
	scanf("%d",&t);

	while (t--)
	{
		cnt=0;
		memset(flag,0,sizeof(flag));
		scanf("%d",&ans1);
		for ( i = 1; i <=4 ; i++)
		{
			for ( j = 1; j <=4 ; j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&ans2);
		for ( i = 1; i <=4 ; i++)
		{
			for ( j = 1; j <=4 ; j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		for ( j = 1; j <=4 ; j++)
		{
			flag[a[ans1][j]]++;
			flag[b[ans2][j]]++;
		}
		for ( i = 1; i <= 16 ; i++)
		{
			if(flag[i]==2){ans=i;cnt++;}
		}
		if(cnt==0)
		{
			printf("Case #%d: Volunteer cheated!\n",++case_num);
		}
		else if(cnt==1)
		{
			printf("Case #%d: %d\n",++case_num,ans);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",++case_num);
		}
	}
	return 0;
}