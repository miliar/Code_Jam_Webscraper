#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <climits>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define len length()
#define mkp make_pair
typedef long long LL;
typedef vector <int> VI;
typedef pair<int, int> PI;

int main()
{
   int t;
   long double r,c,f,x,time;
   cin>>t;
   REP(test,t)
   {
      cin>>c>>f>>x;
      r=2;
      time=0;
      while(x/r>(c/r+x/(f+r)))
      {
         time+=c/r; 
         r+=f;
      }
      time+=x/r;
      printf("Case #%d: %0.7Lf\n",test+1,time);
   }
}




