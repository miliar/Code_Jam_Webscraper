#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<ctime>

using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b)  ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

#define MP make_pair
#define pb push_back
#define inf  1000000000
#define   M  1000000007

#define maxn 1000005
#define maxc 100001
#define MP make_pair

typedef long long LL;
typedef pair<int,int> pi;
typedef pair<pi,pi> pii;
//typedef __int64 LL;

string all[10];
int m,target;
int cost[1<<9];

int calcNodes(int mask)
{
   set<string> S;
   int i,j,ret=1;

   for(i=0;i<m;i++)  if( mask&(1<<i))
   {
      int l=all[i].size();

      for(j=l;j>=1;j--)
      {
         string s=all[i].substr(0,j);
         if(S.find(s)!=S.end()) break;
      }
      ret += (l-j);
      for(j=l;j>=1;j--)
      {
         string s=all[i].substr(0,j);
         S.insert(s);
      }
   }
   cost[mask]=ret;
   return ret;
}

int memo[1<<8][7];
int solve(int mask,int n)
{
   int i,j,ret=-inf;
   if(n==0) return mask==target ? 0 : -inf;
   if(memo[mask][n]!=-1) return  memo[mask][n];

   for (j=target; (j &= ~mask) > 0; j--)
   {
      //if(j==0) continue;
      int q=solve(mask|j,n-1);
      if(q==-inf) continue;
      ret=MAX(ret,cost[j]+q);
    // if(cost[j]+q==11)
         //printf("*%d %d\n",j,q);
   }
  // printf("%d %d %d\n",mask,ret,n);
   return memo[mask][n]=ret;
}

int memo1[1<<8][5][90];

int solve(int mask,int n,int c)
{
   int i,j,ret=0;
   if(n==0) return mask==target && c==0 ? 1 : 0;
   if(memo1[mask][n][c]!=-1) return  memo1[mask][n][c];

   for (j=target; (j &= ~mask) > 0; j--)
   {
      if(c-cost[j]<0) continue;

      int q=solve(mask|j,n-1,c-cost[j]);
      ret=(ret+q)%M;
   }
  // printf("%d %d %d\n",mask,ret,n);
   return memo1[mask][n][c]=ret;
}
int main()
{
	int i,j,k,tests,cs=0,K,n;

	freopen("D-small-attempt0.in","r",stdin);freopen("D-small-attempt0.out","w",stdout);
	//freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{
	   cin>>m>>n;
	   for(i=0;i<m;i++)
         cin>>all[i];

      target  = (1<<m)-1;

      for(i=1;i<(1<<m);i++)
      {
         int ret=calcNodes(i);
         //printf("%d %d\n",i,ret);
      }

      MEM(memo,-1);MEM(memo1,-1);
      int ans1=solve(0,n);
      int ans2=solve(0,n,ans1);

		printf("Case #%d: %d %d\n",++cs,ans1,ans2);
	}

	return 0;
}
