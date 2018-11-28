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


int main()
{
   int i,j,k,T,m,cs=0;
   double c,f,x;

   freopen("D:\\B-large.in","r",stdin);
   freopen("D:\\B-large.txt","w",stdout);

   scanf("%d",&T);

   while(T--)
   {
      cin>>c>>f>>x;

      double r=2.0,ans=0.0,t=0.0;

      for(i=0;;i++)
      {
         double p=i;
         p=2.0+p*f;
         double t1 = x/p;
         double t2 = c/p + x/(p+f);

         if(t1<t2)
         {
            p=2.0;

            for(j=0;j<i;j++)
            {
               ans+=c/p;
               //printf("%lf\n",ans);
               p+=f;
            }
            ans+=x/p;

            break;
         }
      }
      printf("Case #%d: %.9lf\n",++cs,ans);
   }

	return 0;
}
