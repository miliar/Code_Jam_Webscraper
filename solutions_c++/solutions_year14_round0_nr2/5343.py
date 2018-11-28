#include<math.h>
#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<stdio.h>
#include<map>
#include<ext/hash_map>
#include<ext/hash_set>
#include<set>
#include<string>
#include<assert.h>
#include<vector>
#include<time.h>
#include<queue>
#include<deque>
#include<sstream>
#include<stack>
#include<sstream>
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ep 0.0000000001
#define INF 1001001001
#define P 1000000007
#define pr(x) ((x)>=P?(x)-P:(x))
using namespace std;
const int N=100201;
int n,m,i,j,a[4],k;
double c,f,x,s,A,r;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("text.out","w",stdout);
    int t;
    cin>>t;
    int tt=0;
    while (t--)
    {
          tt++;
          cin>>c>>f>>x;
          s=2;
          A=x/s;
          r=0;
          for (i=1;i<=10000000 && r<=x;i++)
          {
              r+=c/s;
              s+=f;
              if (r<=x+0.0000001)   A=MI(A,r+x/s);
              }
                   
      
          printf("Case #%d: %.8lf\n",tt,A);        
          
          }   
    return 0;
}
