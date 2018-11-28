#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int arr[5][5];
int temp[5];
int ans,ansnum;
int n;

void work()
{
	ansnum = 0;
	scanf("%d",&n);
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			scanf("%d",&arr[i][j]);
		}
	for(int i=0;i<4;i++)
		temp[i] = arr[n-1][i];
	scanf("%d",&n);
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			scanf("%d",&arr[i][j]);
		}
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(temp[i] == arr[n-1][j])
			{
				ansnum++;
				ans = temp[i];
			}
	
}
int main()
{
	int cases;
	freopen("A-small-attempt1.in", "r", stdin);
	// freopen("out.out", "w", stdout);
	scanf("%d",&cases);
	for(int Case=1;Case<=cases;Case++)
	{
		
		work();
		printf("Case #%d: ",Case);
		if(ansnum == 0)
			puts("Volunteer cheated!");
		else if(ansnum == 1)
			printf("%d\n",ans);
		else
			puts("Bad magician!");
	}
	return 0;
}