#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

int Case;
int MaxS;
char inp[1002];
int ans;
int now;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_output_large.txt","w",stdout);

	scanf("%d\n",&Case);
	for (int casei=1;casei<=Case;casei++)
	{
		scanf("%d %s\n",&MaxS,inp);
		now=0; ans=0;
		for (int i=0;i<=MaxS;i++)
		{
			if (now<i)
			{
				ans+=i-now;
				now=i;
			}
			now+=inp[i]-'0';
		}
		printf("Case #%d: %d\n",casei,ans);
	}

	return 0;
}
