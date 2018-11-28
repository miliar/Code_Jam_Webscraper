# include <cstdio>
# include <iostream>
# include <map>
# include <list>
# include <map>
# include <vector>
# include <cstring>
# include <string>
# include <set>
# include <climits>
# include <cstdlib>
# include <algorithm>
# include <cmath>
# include<sstream>
# define  MAX 50005
# define  MOD 1000000007
# define  S(x)       scanf("%d",&x)
# define  SL(x)      scanf("%lld",&x)
# define  NL       printf("\n")
# define SP printf(" ")
# define  P(x)       printf("%d",x)
# define  PL(x)      printf("%lld",x)
# define  FOR(i,a)   for(i=0;i<a;i++)
# define  REP(i,a,b) for(i=a;i<=b;i++)
# define REP_IT(it,m) for(it=m.begin();it!=m.end();it++)
# define PB push_back
//string tostr(ll x)     { stringstream ss; ss << x; return ss.str(); }
//ll toint(string &s)    { stringstream ss; ss << s; long long x; ss >> x; return x; }
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
using namespace std;
int arr[2000];
int main()
{
freopen("in.txt","rt",stdin);
freopen("out.txt","wt",stdout);
int t,test,a,b,i,ans;
arr[1]=1;
arr[4]=1;
arr[9]=1;
arr[121]=1;
arr[484]=1;
S(test);

REP(t,1,test)
{
    S(a);S(b);
    ans=0;
    REP(i,a,b)
    {
        if(arr[i]==1)
        ans++;
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
}
return 0;
}
