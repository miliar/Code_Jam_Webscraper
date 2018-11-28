
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<sstream>

#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef pair<int,int> pii;
typedef long long int lld;
typedef long double Lf;
typedef unsigned long long int llu;
   template <typename T>
ostream& operator <<(ostream &o,vector < T >  &v)
{
   for(typeof(v.size()) i=0;i<v.size();++i)
      o<<v[i]<<" ";
   o<<endl;
   return o;
}
template < class T1, class T2, class T3 > 
struct trio{
   T1 first;
   T2 second;
   T3 third;
   trio(): first(T1()),second(T2()),third(T3()){}
   trio(const T1 &x, const T2 &y, const T3 &z): first(x),second(y),third(z){}
   template < class X, class Y, class Z >
      trio (const trio < X, Y , Z > &p) : first(p.first),second(p.second), third(p.third){}

};
typedef trio < int, int , int > tiii;
   template < class T1, class T2, class T3 > 
bool operator < (const trio < T1, T2 , T3 > &x,const trio < T1, T2 , T3 > &y)
{
   if(x.first<y.first) return true;
   else if(x.first> y.first) return false;
   if(x.second<y.second) return true;
   else if(x.second> y.second) return false;
   if(x.third<y.third) return true;
   else if(x.third> y.third) return false;
   return false;
}

#define sz(a)                        int((a).size()) 
#define pb                           push_back 
#define mp                           make_pair
#define F                            first
#define S                            second
#define present(c,x)                 ((c).find(x) != (c).end()) 
#define cpresent(c,x)                (find(all(c),x) != (c).end())
#define tr(c,i)                      for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rtr(c,i)                      for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c)                       (c).begin(),(c).end()
#define si(n)                        scanf("%d",&n)
#define sl(n)                        scanf("%lld",&n)
#define sf(n)                        scanf("%f",&n)
#define sd(n)                        scanf("%lf",&n)
#define ss(n)                        scanf("%s",n)
template<typename T,typename U>
ostream &operator <<(ostream &o,const pair< T,U  > &x)
{
  o<< x.first <<","<< x.second <<" ";
  return o;
}
  template <typename T>
istream& operator >>(istream &i,vector < T >  &v)
{
  int n;
  i>>n;
  while(n--){
    int x;
    i>>x;
    v.pb(x);
  }
  return i;
}
#define abs(x)                       ((x)<0?-(x):(x))
#define fill(a,v)                    memset((a),(v),sizeof (a))
#define INF                          INT_MAX
#define LINF                         (long long)1e18
#define EPS                          1e-9
#define MODBY 1000000007
#define MAX                          
int preprocess()
{
   int ans=0;
   return ans;
}
int main()
{
   preprocess();
   int i,j,n;
   int cases;
   int cno=1;
   for(scanf("%d",&cases);cases;--cases,++cno){
      printf("Case #%d: ",cno);
      Lf c,f,x;
      cin>>c>>f>>x;
      Lf hi=x;
      Lf lo=0;
      for(int i=0;i<100;++i){
         Lf mid=(hi+lo)/2;
         int poss=0;
         Lf rate=2;
         Lf t=0;
         if(mid*rate >=x){//no factories at all!!
            hi=mid;
            continue;
         }
         while(1){
            //you have 0 cookies at time t and some factories, which are counted in rate
            //// you must create at least one factory
            ////only create profitable factories
            Lf dt = c/rate;
            if((t+dt > mid - c/f)) break;//failure
            else{
               t+=dt;
               rate+=f;
               if((mid-t)*rate>=x){
                  poss=1;
                  break;
               }
            }
         }
         if(poss)
            hi=mid;
         else
            lo=mid;
      }
      printf("%0.7Lf\n",hi);
   }
   return 0;
}
