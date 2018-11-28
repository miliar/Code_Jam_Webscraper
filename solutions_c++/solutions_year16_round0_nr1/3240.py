#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int T, n, cnt;
int ans, x;
bool visited[12];

void clear()
{
	for (int i=0;i<=9;i++)
		visited[i]=false;
}

bool check()
{
	for (int i=0;i<=9;i++)
	if (!visited[i])
		return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d",&T);
	for (int k=1;k<=T;k++)
	{
		cnt=1;
		clear();
		scanf("%d",&ans);
		
		printf("Case #%d: ",k);
		if (ans==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		
		while (!check())
		{
			x=ans*cnt;
			while (x)
			{
				visited[x%10]=true;
				x/=10;
			}
			cnt++;
			if (cnt>=100)
			{
				printf("INSOMNIA\n");
				break;
			}
		}
		printf("%d\n",ans*(cnt-1));
	}
	
	fclose(stdin);
	fclose(stdout);			
	return 0;
}











		
