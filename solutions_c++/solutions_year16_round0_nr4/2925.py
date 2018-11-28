#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%ld",&n)
#define sll(n)                      scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ssp(n)                      scanf("%[^\n]%*c",n)
#define prt(x)        	            printf("%d\n",x);
#define plt(x)				printf("%lld\n",x);

#define INF                   	0x3f3f3f3f
#define EPS                         1e-12

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define rall(a)                     a.rbegin(),a.rend()

#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define dot(a,b)                    ((conj(a)*(b)).X)
#define cross(a,b)                  ((conj(a)*(b)).imag())
#define normalize(v)                ((v)/length(v))
#define rotate(p,about,theta)       ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b)               (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef stringstream ss;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<vector<int> > vvi;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}
#define SMALL
//#define LARGE

int main()
{

#ifdef SMALL
      freopen("D-small-attempt0.in","rt",stdin);
      freopen("D-small.out","wt",stdout);
#endif
#ifdef LARGE
      freopen("D-large.in","rt",stdin);
      freopen("D-large.out","wt",stdout);
#endif

int t,k,c,s;
s(t);

forall(i,1,t+1)
{
      s(k);
      s(c);
      s(s);

      printf("Case #%d: ",i);
      if(s!=k)
            printf("IMPOSSIBLE\n");
      else
      {
            forall(j,1,k)
                  printf("%d ",j);
            printf("%d\n",k);      
      }
}

return 0;
}