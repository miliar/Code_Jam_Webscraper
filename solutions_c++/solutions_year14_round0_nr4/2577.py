#include<iostream>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t;
int n;
double me[2000];
double you[2000];

bool cmp(const double a, const double b)
{
	if(a>b)
		return true;
	return false;
}

void init()
{
	memset(me,0,sizeof(me));
	memset(you,0,sizeof(you));
	return;
}

int main()
{
	freopen("D1.in", "r", stdin);
	freopen("D2.txt", "w", stdout);
	cin>>t;
	for(int files=1; files<=t;files++)
	{
		cin>>n;
		
		init();
		int i;
		for(i=1;i<=n;i++)
			cin>>me[i];
		for(i=1;i<=n;i++)
			cin>>you[i];
		
		sort(&me[1], &me[n+1], cmp);
		sort(&you[1], &you[n+1], cmp);
		
		int j;
		int ans1=0, ans2=0;
		int head=1, tail=n;
		for(i=n;i>=1;i--)
		{
			if(me[i]<you[tail])
			{
				head++;
			}
			else
			{
				ans1++;
				tail--;
			}
		}
		
		head=1;
		tail=n;
		for(i=1;i<=n;i++)
		{
			if(me[i]>you[head])
			{
				ans2++;
				tail--;
			}
			else
			{
				head++;
			}
		}
		
		printf("Case #%d: %d %d\n", files, ans1, ans2);
		
	}
	//system("pause");
	return 0;
}