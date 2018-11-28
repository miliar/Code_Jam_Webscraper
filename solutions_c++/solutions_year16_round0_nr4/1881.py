#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("d_ans.out","w",stdout);
	int cnt;scanf("%d",&cnt);
	for(int e=1;e<=cnt;e++)
	{
		int k,c,s;
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d: ",e);
		for(int i = 1;i<=k;i++)
			printf("%d ",i);
		printf("\n");
	}
}
