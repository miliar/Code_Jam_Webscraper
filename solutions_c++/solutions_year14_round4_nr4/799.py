#include <bits/stdc++.h>
using namespace std;
bool A[500][500];
int R[1000] , C[1000] , S[1000];
struct pt
{
	int x , y;
	/* data */
};
bool match(int i , int m )
{
	for (int j = 0; j < m; ++j)
	{
		if(A[i][j]&&(!S[j]))
		{
			S[j]=1;
			if(C[j]<0||match(C[j],m))
			{
				C[j]=i;
				R[i]=j;
				return true;
			}
		}
	}
	return false;
}
int max_matching(int n , int m)
{
	memset(R,-1,sizeof R);
	memset(C,-1,sizeof C);
	int ans=0;
	for(int i =0 ;i<n ;i++)
	{
		memset(S,false,sizeof S);
		if(match(i,m))ans++;
	}
	return ans;
}

int main()
{
	int t ;
	scanf("%d",&t);
	while(t--)
	{
		int n , m , s , c;
		scanf("%d%d%d%d",&n,&m,&s,&c);
		pt people[1000] , taxi[1000];
		for(int i =0 ;i<n;i++)
			scanf("%d%d",&people[i].x,&people[i].y);
		for(int i=0;i<m;i++)
			scanf("%d%d",&taxi[i].x,&taxi[i].y);
		memset(A,false,sizeof A);
		for(int i =0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				long long int p = (abs(people[i].x-taxi[j].x)+abs(people[i].y-taxi[j].y))*200LL;
				if(p<=(long long )s*(long long)c)A[i][j]=true;
			}
		}
		int ans = max_matching(n,m);
		printf("%d\n",ans );
	}
	return 0;
}