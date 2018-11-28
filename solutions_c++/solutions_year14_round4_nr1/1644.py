#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;

int t;
int n;
int x;

int a[10010];

void init()
{
	memset(a,0,sizeof(a));
	return ;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A1.txt", "w",stdout);
	scanf("%d", &t);
	int files;
	for(files=1; files<=t;files++)
	{
		init();
		scanf("%d %d", &n, &x);
		int i;
		for(i=1;i<=n;i++)
			    scanf("%d", &a[i]);
		
		sort(a+1, a+n+1);
		int p1 = 1;
		int p2 = n;
		
		int ans = 0;
		while(p1 <= p2)
		{
			if(p1==p2)
			{
				ans++;
				break;
			}
			if(a[p2] + a[p1] <= x)
			{
				p2--;
				p1++;
			}
			else
			{
				p2--;
			}
			ans++;
		}
		printf("Case #%d: %d\n", files, ans);
	}
//	system("pause");
	return 0;
}