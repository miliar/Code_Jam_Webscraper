#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <utility>
#include <algorithm>
#include <limits>
#include <time.h>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <map>
#include <set>

#define FOR(i,a,b) for (int i=a; i<=b; i++)
#define FORD(i,a,b) for (int i=a; i>=b; i--)
#define p_b push_back
#define m_p make_pair
#define eps 1e-12
#define F first
#define S second
#define INF numeric_limits <int> :: max()
#define tr(Con,it) for(typeof(Con.begin()) it=Con.begin();it!=Con.end();it++)

using namespace std;    
int T;
double c,f,x,persec,ans,t;
int main()
{
 #ifndef ONLINE_JUDGE
 freopen("input.txt","rt",stdin);
 freopen("output.txt","wt",stdout);
 #endif 
 scanf("%d\n",&T);
 FOR(q,1,T)
  {
   cin>>c>>f>>x;
   persec=2.0;
   ans=x/persec;
   t=0.0;
   FOR(i,1,INF)
    {
     t=t+((c*1.0)/(persec*1.0));
     persec+=f;

     if (t+(x*1.0/persec*1.0) < ans)
      {
       ans=t+(x*1.0/persec*1.0);
      } else break;

    }

   printf("Case #%d: %.7lf\n",q,ans);
  }

 return 0;
}
