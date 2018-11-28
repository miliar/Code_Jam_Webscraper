#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<string>
using namespace std;
typedef long long lld;
int ok[110];
int s[110][110];
void fill()
{
	int r;
	scanf("%d",&r);
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
			scanf("%d",&s[i][j]);
	for(int j=1;j<=4;j++)
		ok[s[r][j]]++;
}
int pp[110];
int qq;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		memset(ok,0,sizeof(ok));
		fill();
		fill();
		qq=0;
		for(int i=1;i<=16;i++)
			if(ok[i] == 2)
				pp[qq++]=i;
		printf("Case #%d: ",cc);
		if(qq == 0)
			printf("Volunteer cheated!\n");
		else if(qq == 1)
			printf("%d\n",pp[0]);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
/*
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

 */
