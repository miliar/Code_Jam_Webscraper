#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <string>
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n)					scanf("%d",&n)
#define Sl(n)					scanf("%lld",&n)
#define Sf(n) 					scanf("%lf",&n)
#define Ss(n) 					scanf("%s",n)
using namespace std;
int arr[110][110];
int rowm[110];
int colm[110];
//int cur[110][110];
bool cut(int row,int col)
{
	int i,j,k;
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			if(arr[i][j]<min(rowm[i],colm[j]))
			return false;
		}
	}
	return true;
}
int main()
{
	int i,j,k,l,m,n,t;
	#ifndef ONLINE_JUDGE
	freopen("test2.in","r",stdin);
	freopen("op2.txt","w",stdout);
	#endif
	S(t);
	k=1;
	while(t--)
	{
		S(n),S(m);
		for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		S(arr[i][j]);
		
		for(i=0;i<n;i++)
		{
			rowm[i]=-1;
			for(j=0;j<m;j++)
			rowm[i]=max(rowm[i],arr[i][j]);
		}
		
		for(j=0;j<m;j++)
		{
			colm[j]=-1;
			for(i=0;i<n;i++)
			colm[j]=max(colm[j],arr[i][j]);
		}
		
		if(cut(n,m))
		printf("Case #%d: YES\n",k++);
		else
		printf("Case #%d: NO\n",k++);
		
		
		
		
		
	}
	return 0;
}
