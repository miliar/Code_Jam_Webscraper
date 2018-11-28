#include <cassert>
#include <cctype>
//#include <cinttypes>
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
#define prt(x)                      printf("%d\n",x);
#define plt(x)                      printf("%lld\n",x);

#define INF                         0x3f3f3f3f
#define EPS                         1e-12

#define bitcount                    __builtin_popcount
#define bitcountl                   __builtin_popcountl
#define bitcountll                  __builtin_popcountll
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
#define strjoin( x, y )              x ## y
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
#define MOD
#define ADD(X,Y)                     ((X) = ((X) + (Y)%MOD) % MOD)

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


//#define DEBUG
#ifdef DEBUG
      #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
      #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
      #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
      #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
      #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
      #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
      #define trace1(x)           
      #define trace2(x,y)         
      #define trace3(x,y,z)       
      #define trace4(a,b,c,d)     
      #define trace5(a,b,c,d,e)   
      #define trace6(a,b,c,d,e,f) 
#endif

//#define SMALL
#define LARGE


struct senate
{
      int ctr;
      char pt;
      bool operator ()(senate s2, senate s3){ return (s2.ctr>s3.ctr); }
}s1,myob;

int main()
{

#ifdef SMALL
      freopen("A-small-attempt0.in","rt",stdin);
      freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
      freopen("A-large.in","rt",stdin);
      freopen("A-large.out","wt",stdout);
#endif

int t,n,count;
vector<senate> sn;
s(t);
forall(w,1,t+1)
{
      sn.clear();
      trace1(sn.size());
      count=0;
      s(n);
      forall(v,0,n)
      {
            int ct;
            char st;
            s(ct);
            count+=ct;
            st=(char)(v+65);
            s1.ctr=ct;
            s1.pt=st;

            sn.pb(s1);
            trace1(sn.size());
      }
      //printf("Case #%d: %d\n",w,ans);
      cout<<"Case #"<<w<<": ";
      sort(all(sn),myob);
      int k=0;
      while(1)
      {
            s1=sn[0];
            if(s1.ctr==0)
                  break;
            else if(count==1)
            {
                  s1=sn[0];
                  cout<<s1.pt;
                  break;
            }
            else if(k>0)
                  cout<<" ";

            bool flag=true;
            int cst=floor((count-2)/2);
            forall(p,0,sn.size())
            {
                  s1=sn[p];
                  if(p<=1) 
                  {
                        if((s1.ctr-1)>cst)
                        {     trace3(s1.ctr,cst,p);
                              flag=false;
                              break;
                        }
                  }
                  else if(s1.ctr>cst)
                  {
                        trace3(s1.ctr,cst,p);
                         flag=false;
                         break;
                  }     
            }
            if(flag)
            { 
                  
                  s1=sn[0];
                  s1.ctr-=1;
                  cout<<s1.pt;
                  sn[0]=s1;


                  s1=sn[1];
                  s1.ctr-=1;
                  cout<<s1.pt;
                  //sn.insert(sn.begin()+1,s1);
                  sn[1]=s1;

                  count-=2;
            }
            else
            {
                  s1=sn[0];
                  s1.ctr-=1;
                  cout<<s1.pt;
                  sn[0]=s1;

                  count--;          
            }
            
           sort(all(sn),myob); 
            k++;
      }
      cout<<endl;
}
return 0;
}           