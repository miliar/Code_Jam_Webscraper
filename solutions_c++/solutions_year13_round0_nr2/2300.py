/* Author : migdal */
#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;
#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define INF 1000000000
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;
int n,m,mat[11][11];
int check(int r,int c)
{
   int i,j;
   int f1=0,f2=0;
   for(i=1;i<=m;i++)if(mat[r][i]==2)f1=1;
   for(j=1;j<=n;j++)if(mat[j][c]==2)f2=1;
   if(f2==1&&f1==1)return 0;
   else return 1;
}
int main()
{
   int test,i,j,coun,fl;
   cin>>test;coun=0;
   while(test--)
   {
      fl=0;
      coun++;
      cin>>n>>m;
      for(i=1;i<=n;i++)for(j=1;j<=m;j++)cin>>mat[i][j];
      for(i=1;i<=n;i++)for(j=1;j<=m;j++)if(mat[i][j]==1&&!check(i,j))fl=1;
      if(fl)cout<<"Case #"<<coun<<": "<<"NO"<<endl;
      else cout<<"Case #"<<coun<<": "<<"YES"<<endl;
   }
   return 0;
}
