#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;
 
#define ll long long
#define ld long double
#define Fox(i,n) for (i=0; i<n; i++)
#define Fox1(i,n) for (i=1; i<=n; i++)
#define FoxI(i,a,b) for (i=a; i<=b; i++)
#define FoxR(i,n) for (i=n-1; i>=0; i--)
#define FoxR1(i,n) for (i=n; i>0; i--)
#define FoxRI(i,a,b) for (i=b; i>=a; i--)
#define Foxen(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define sz(s) int((s).size())
#define all(s) (s).begin(),(s).end()
#define FILL(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define rep(i,a,n) for (int i=a;i<(int)n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<ll> vl;
const ll mod=1000000007;
const double eps=1e-9;
const double pi=acos(0)*2;


int main()
{ int t,ch=0;
  double f,x,cps,cookies=0,c,time;
  cin>>t;
  while(t--)
   { ++ch;
     cps=2;
     cin>>c>>f>>x;
     time=0;
     while(1)
       { if ( (x/cps) <= ( (c/cps) + (x/(cps+f)) ) )break; 
       	 time+=(c/cps);
       	 cps+=f;
       }
     time+=(x/cps); 
   	 printf("Case #%d: %.7f\n",ch,time);
   }
  return 0;	
}
