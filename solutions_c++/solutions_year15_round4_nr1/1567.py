#pragma comment(linker,"/STACK:102400000,102400000")
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstdlib>
#include<functional>
#include<bitset>
using namespace std;
const double eps=1e-9;
const double pi=acos(-1.0);
const int mod=1000000007;
#define N 111
char c[N][N];
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("ans2.txt","w",stdout); 
	int i,j,k,t,tt=0;
	int n,m;
	scanf("%d",&t);
	while(t--)
	{
		bool f=true;
		scanf("%d%d",&n,&m);
		memset(c,'#',sizeof(c));
		for(i=1;i<=n;i++)
		{
			scanf("%s",c[i]+1);
			c[i][m+1]='#';
		}
		int ans=0;
		for(i=1;f&&i<=n;i++)
			for(j=1;f&&j<=m;j++)
			{
				if(c[i][j]=='<')
				{
					bool b=false;
					for(k=j-1;b==false&&k;k--)
						if(c[i][k]!='.')
							b=true;
					ans+=b==false;
					for(k=j+1;b==false&&k<=m;k++)
						if(c[i][k]!='.')
							b=true;
					for(k=i-1;b==false&&k;k--)
						if(c[k][j]!='.')
							b=true;
					for(k=i+1;b==false&&k<=n;k++)
						if(c[k][j]!='.')
							b=true;
					if(b==false)
						f=false;
				}
				if(c[i][j]=='>')
				{
					bool b=false;
					for(k=j+1;b==false&&k<=m;k++)
						if(c[i][k]!='.')
							b=true;
					ans+=b==false;
					for(k=j-1;b==false&&k;k--)
						if(c[i][k]!='.')
							b=true;
					for(k=i-1;b==false&&k;k--)
						if(c[k][j]!='.')
							b=true;
					for(k=i+1;b==false&&k<=n;k++)
						if(c[k][j]!='.')
							b=true;
					if(b==false)
						f=false;
				}
				if(c[i][j]=='^')
				{
					bool b=false;
					for(k=i-1;b==false&&k;k--)
						if(c[k][j]!='.')
							b=true;
					ans+=b==false;
					for(k=j-1;b==false&&k;k--)
						if(c[i][k]!='.')
							b=true;
					for(k=j+1;b==false&&k<=m;k++)
						if(c[i][k]!='.')
							b=true;
					for(k=i+1;b==false&&k<=n;k++)
						if(c[k][j]!='.')
							b=true;
					if(b==false)
						f=false;
				}
				if(c[i][j]=='v')
				{
					bool b=false;
					for(k=i+1;b==false&&k<=n;k++)
						if(c[k][j]!='.')
							b=true;
					ans+=b==false;
					for(k=j-1;b==false&&k;k--)
						if(c[i][k]!='.')
							b=true;
					for(k=j+1;b==false&&k<=m;k++)
						if(c[i][k]!='.')
							b=true;
					for(k=i-1;b==false&&k;k--)
						if(c[k][j]!='.')
							b=true;
					if(b==false)
						f=false;
				}
			}
		printf("Case #%d: ",++tt);
		if(f==false)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
/*
99
2 2
..
^^

2 1
v
.
2 1
<
>
2 2
<.
<>
2 2
<.
..

*/
/*
99
2 1
^
^
2 2
>v
^<
3 3
...
.^.
...
1 1
.

Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 0
*/
