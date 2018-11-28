#include<math.h>
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<time.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

//typedef long long lld;
//typedef __int64 lld;//这里的时候要用long long
const int INF=1000000000;
const int MAX=1100;
bool para[MAX];
bool ok(int n)
{
	int bit[111],len=0,i;
	for(i=0;n;i++)
	{
		bit[i]=n%10;
		n/=10;
	}
	int j=0;
	for(i--;j<=i;i--,j++)
	{
		if(bit[i]!=bit[j])return false;
	}
	return true;
}
int main()
{
	int n,m;
	int i,j;
	int ans=INF;
	int T,CS=1;
//	freopen("E:\\ACM\\C-small-attempt0.in","r",stdin);
	//freopen("E:\\ACM\\C-small-attempt0.out","w",stdout);
	for(i=1;i<MAX;i++)
	{
		para[i]=ok(i);
	}
	scanf("%d",&T);
	while(T--)
	{
		int ans=0;
		scanf("%d%d",&n,&m);
		for(i=1;i*i<=m;i++)
		{
			if(para[i]&&para[i*i]&&i*i>=n&&i*i<=m)
				ans++;
		}
		printf("Case #%d: %d\n",CS++,ans);
	}
	return 0;
}
/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

*/
