#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <set>
#include <stack>
#include <deque>
#include <cmath>
using namespace std;
#define ll long long
#define N 100005
#define eps 1e-7
#define lson l,m,x<<1
#define rson m+1,r,x<<1|1
int vis[15];
int judge()
{
	int i;
	for(i = 0;i<= 9;i++)
	{
		if(vis[i] == 0)
			return 0;
	}
	return 1;
}
int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int p=0;
	while(t--)
	{
		memset(vis,0,sizeof(vis));
		p++;
		int n;
		scanf("%d",&n);
		int q =n;
		printf("Case #%d: ",p);
		int i;
		if(n == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		for(i = 1;;i++)
		{
			n =i*q;
			int m; 
			m =n;
			while(m)
			{
				vis[m%10] = 1;
				m /=10;
			}
			if(judge()) break;
		}
		printf("%d\n",i*q);
	}
} 
