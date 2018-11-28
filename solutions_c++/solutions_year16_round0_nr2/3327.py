#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
char str[100010];
char f[2]={'+','-'};
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B_large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%s",str);
		int ans=0;
		int at=1;
		for(int i=strlen(str);i>=0;i--)
		{
			if(str[i] == f[at])
			{
				ans++;
				at^=1;
			}
		}
		printf("Case #%d: %d\n",cc,ans);
	}
    return 0;
}
/*
5
-
-+
+-
+++
--+-

 */
