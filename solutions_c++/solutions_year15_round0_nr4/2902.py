#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }

#define ALL(p) p.begin(),p.end()
#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define root 1
#define lft 2*idx
#define rgt 2*idx+1
#define cllft lft,st,mid
#define clrgt rgt,mid+1,ed
#define i64 long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define MX 1000009

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;


int main()
{
// 
int k,t;
scanf("%d",&k);
t=k;
while(k--)
{
int x,r,c;
scanf("%d %d %d",&x,&r,&c);
int sum =0,n=0,flag=0;
sum =r*c;
int y=x;
while(y>=1)
{
    if(sum%x!=0)
        break;
if(sum%y!=0)
  {
      if(c<=r)
      { c=c-1;
      if(c==0)
      flag=0;
        while(c)
        {
            n=c*r;
            if(n%y!=0)
            flag=0;
            else
            flag=1;
             if(flag==1)
                break;
                c--;
        }
      }
      if(r<c)
      { r=r-1;
      if(r==0)
        flag=0;
        while(r)
        {
            n=c*r;
            if(n%y!=0)
            flag=0;
            else
                flag=1;
                if(flag==1)
                    break;
                r--;
        }
      }
  }
  else
  flag=1;
  if(flag==0)
    break;
  y--;
}
if(flag==1)
printf("Case #%d: GABRIEL\n",t-k);
else
printf("Case #%d: RICHARD\n",t-k);
}
return 0;
}

