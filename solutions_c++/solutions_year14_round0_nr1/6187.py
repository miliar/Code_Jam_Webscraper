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
   int t,x,y,count,ind;
   set <int> s;
   int a[10][10],b[10][10];
   cin>>t;
   REP(test,t)
   {
       count=0;
       cin>>x;
       REP(i,4)
        REP(j,4)
            cin>>a[i][j];
         
       cin>>y;
       REP(i,4)
        REP(j,4)
         {
            cin>>b[i][j];
            if(y==i+1)
              REP(k,4)
                 if(a[x-1][k]==b[i][j])
                 {
                     count++;
                     ind=a[x-1][k];
                 }
         }
       if(count==1)
            cout<<"Case #"<<test+1<<": "<<ind<<"\n";
       else if(count>1)
            cout<<"Case #"<<test+1<<": Bad magician!\n";
       else
            cout<<"Case #"<<test+1<<": Volunteer cheated!\n";

   }
}




