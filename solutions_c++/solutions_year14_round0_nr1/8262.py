#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<cstdio>
#include <ctime>
#include<cassert>
#include <pthread.h>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MP make_pair
#define pb push_back


#define maxn 10000
#define maxt 100
#define maxv 1000000

#define inf  1000000000
#define   M  1000000007

typedef long long  LL;

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

int grid1[5][5],grid2[5][5];
int row[20];

int main()
{
   int i,j,k,T,m,cs=0;
   double c,f,x;

   freopen("D:\\A-small-attempt0.in","r",stdin);
   freopen("D:\\A-small-attempt0.txt","w",stdout);

   scanf("%d",&T);

   while(T--)
   {
      int r1,r2;
      cin>>r1;
      --r1;
      for(i=0;i<4;i++)
         for(j=0;j<4;j++) cin>>grid1[i][j];

      cin>>r2;
      --r2;
      for(i=0;i<4;i++)
         for(j=0;j<4;j++)
         {
            cin>>k;
            row[k]=i;
         }

      int cnt=0,ans=-1;

      for(i=0;i<4;i++)
      {

         int c=grid1[r1][i];

         if(row[c]==r2)
            cnt++,ans=c;
      }

      printf("Case #%d: ",++cs);
      if(cnt==0)
         puts("Volunteer cheated!");
      else if(cnt>1)
         puts("Bad magician!");
      else
         printf("%d\n",ans);
   }

	return 0;
}
