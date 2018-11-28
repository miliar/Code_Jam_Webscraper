//adhoc google code jam

#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<iomanip>
#include<math.h>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#define mod 1000000007
#define MAX 100000000

using namespace std;

#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(),a.end())
#define INF 1000000000
#define V vector
#define S string
typedef long long LL;
typedef long double LD;
typedef long L;
typedef pair<int, int> p;
const double pi=acos(-1.0);
int main()
{
  int t,cn=1;
  scanf("%d",&t);
  while(t--)
  {
    LD c,f,x,ansc=0,ansx,anst=0,r=2,cnt=0,m,k;
    scanf("%llf %llf %llf",&c,&f,&x);
    m=x/r;
    k=c/r;
    if(m<=k)
    {
      printf("Case #%d: %.7llf\n",cn++,m);                
    }
    else
    {
      ansx=x/r;
      while(ansx>=anst)
      { 
         ansc+=c/r;
         r+=f;
         anst=ansc;
         anst+=x/r;
         if(anst<ansx)
         {
           ansx=anst;
         }
      }
      printf("Case #%d: %.7llf\n",cn++,ansx);
    }          
  }    
  return 0;
}
