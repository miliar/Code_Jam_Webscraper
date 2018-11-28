#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;

int t;
int d;
int p[1010];

void init()
{
	memset(p,0,sizeof(p));
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	for(int files=1; files<=t; files++)
	{
		init();
		scanf("%d", &d);
		int i,j;
		int max_num=0;
		for(i=1;i<=d;i++)
		{
			scanf("%d", &p[i]);
			max_num = max(max_num, p[i]);
		}
		
		int ans = max_num;
		for(i=1; i<=max_num; i++)
		{
			int sum_divide = 0;
			for(j=1; j<=d; j++)
			{
				sum_divide += (p[j]-1)/i;
			}
			ans = min(ans, sum_divide + i);
		}
		
		printf("Case #%d: %d\n", files, ans);
		
	}
	//system("pause");
	return 0;
}












