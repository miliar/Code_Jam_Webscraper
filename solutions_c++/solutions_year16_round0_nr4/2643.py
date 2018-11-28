#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int T, k, s, c;
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	
	scanf("%d",&T);
	for (int j=1;j<=T;j++)
	{
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:", j);
		for (int i=1;i<=s;i++)
			printf(" %d", i);
		printf("\n");
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}





