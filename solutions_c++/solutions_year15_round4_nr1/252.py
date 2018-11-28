#include <bits/stdc++.h>
using namespace std;

const int N = 1e2 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

char tab[N][N];
int ile[N][N];
bool chan[N][N];
char x[5] = {'^','v','<','>','.'};

int test()
{
	int r,c;
	scanf("%d%d",&r,&c);
	for (int i=0;i<r;i++)
		scanf("%s",tab[i]);
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++)
			ile[i][j] = chan[i][j] =  0;
	for (int i=0;i<r;i++)
	{
		for (int j=0;j<c;j++)
			if ( tab[i][j] != x[4] )
			{
				if ( tab[i][j] == x[2] ) chan[i][j] = 1;
				ile[i][j] ++;
				break;
			}
		for (int j=c-1;j>=0;j--)
			if ( tab[i][j] != x[4] )
			{
				if ( tab[i][j] == x[3] ) chan[i][j] = 1;
				ile[i][j] ++;
				break;
			}
	}
	for (int j=0;j<c;j++)
	{
		for (int i=0;i<r;i++)
			if ( tab[i][j] != x[4] )
			{
				if ( tab[i][j] == x[0] ) chan[i][j] = 1;
				ile[i][j] ++;
				break;
			}
		for (int i=r-1;i>=0;i--)
			if ( tab[i][j] != x[4] )
			{
				if ( tab[i][j] == x[1] ) chan[i][j] = 1;
				ile[i][j] ++;
				break;
			}
	}
	bool OK = 1;
	int suma = 0;
	for (int i=0;i<r;i++)
	{
		for (int j=0;j<c;j++)
		{
//			printf("%d ",ile[i][j] );
			if ( ile[i][j] )
			{
				if ( ile[i][j] == 4 ) OK = 0;
				if ( chan[i][j] ) suma ++;
			}
		}
//		printf("\n");
	}
	if ( OK == 0 ) printf("IMPOSSIBLE");
	else printf("%d",suma);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		test();
		printf("\n");
	}
}
