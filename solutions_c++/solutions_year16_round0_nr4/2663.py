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
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D_small.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int k,c,s;
		scanf("%d %d %d",&k,&c,&s);
		printf("Case #%d:",cc);
		for(int i=1;i<=s;i++)
			printf(" %d",i);
		printf("\n");
	}
    return 0;
}
/*
1
6 3

 */
