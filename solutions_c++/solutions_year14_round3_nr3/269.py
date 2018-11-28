#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

bool flag = 0, vis[55][55],v[55][55];
int N,M,K;

int flood(int r,int c)
{
	if(r>=N || c>=M || r<0 || c<0)
	{
		flag = 1;
		return 0;
	}
	
	if(v[r][c])return 0;
	if(vis[r][c])return 0;
	
	v[r][c]=1;
	
	return 1+flood(r+1,c) + flood(r-1,c) + flood(r,c+1) + flood(r,c-1);
}

int main()
{
    freopen ("C-small-attempt0.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int T,k=0;
    scanf("%d",&T);
    
    while(T--)
    {
		int ret=1<<30;
		k++;
		printf("Case #%d: ",k);
		
		scanf("%d %d %d",&N,&M,&K);
		
		for(int i=0;i<(1<<N*M);i++)
		{
			int r=0;
			for(int j=0;j<N*M;j++)
			{
				if(i&(1<<j))
				{
					r++;
					vis[j/M][j%M] = 1;
				}
			}
			
			for(int p=0;p<N;p++)
			{
				for(int q=0;q<M;q++)
				{
					flag = 0;
					int x = flood(p,q);
					if(x + r >= K && !flag)
						ret=min(ret,r);
				}
			}
			
			for(int p=0;p<N;p++)
			{
				for(int q=0;q<M;q++)
				{
					v[p][q]=0;
				}
			}
			
			
			for(int j=0;j<N*M;j++)
			{
				if(i&(1<<j))
				{
					vis[j/M][j%M] = 0;
				}
			}
		}
		printf("%d\n",ret);
	}
}


































