#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <utility>
using namespace std;

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }

#define ALL(c) c.begin(), c.end()
#define PB(x) push_back(x)
#define UB(s, e, x) upper_bound(s, e, x)
#define LB(s, e, x) lower_bound(s, e, x)
#define REV(s, e) reverse(s, e);
#define SZ(c) c.size()
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define ll long long
#define ff first
#define ss second
#define DEBUG if(0)

#define si(x) scanf("%d",&x)
#define pi(x) printf("%d\n",x)
#define siz 100100
int main()
{
    //ios_base::sync_with_stdio(0);
    freopen("in.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int t,x=1;
    cin>>t;
    while(t--)
    {
    string str;
    int n,i,j,ans=0,sum=0,a[1010];
    cin>>n;
    cin>>str;
    n++;   
    for(i=n-1;i>=0;i--)
    if(str[i]!='0')
    break;
    str[i+1]='\0';
    n=i+1;
     for(i=0;i<n;i++)
      a[i]=str[i]-'0';
      for(i=1;i<n;i++)
      a[i]+=a[i-1];   
    for(i=1;i<n;i++)
    {
      if(i-a[i-1]-ans>0)
      ans+=i-a[i-1]-ans;
        
      }                     
    
    cout<<"Case #"<<x++<<": "<<ans<<'\n';
    }
    return 0;
} 
    
