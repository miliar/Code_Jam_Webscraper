#include<cassert>
#include<queue>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<iostream>
#include<algorithm>

#define eps 1e-12

#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair(a,b) 
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define taskname ""
#ifdef DEBUG
#define deb(x) cerr<<#x<<'='<<x<<endl
#else
#define deb(x) 
#endif
typedef long long ll;

using namespace std;

ll best(ll i, ll n){
   ll len = (1ll << n) - i - 1;
   ll place = (1ll << n);
   while(len){
     len = (len - 1) / 2;
     place /= 2;
   }
   return place;
}
ll worst(ll i, ll n){
  ll len = i;
  ll down = (1ll << (n - 1));
  ll place = 1ll;
  while(len){
    len = (len - 1) / 2;
    place += down;
    down /= 2;
  }
  return place;
}
int main()         
{
  assert(freopen(taskname"in","r",stdin));
  assert(freopen(taskname"out","w",stdout));
  int test_n;
  scanf("%d",&test_n);
  forn(test_id,test_n)
  {
    printf("Case #%d: ",test_id+1);
    ll n,p;
    cin >> n >> p;
    ll l = 0, r = 1ll << n;
    while(l != r - 1){
      ll m = (l + r) / 2;
      if(worst(m, n) <= p)
        l = m;
      else
        r = m;      
    }
    cout << l << " ";
    l = 0, r = 1ll << n;
    while(l != r - 1){
      ll m = (l + r) / 2;
      if(best(m, n) <= p)
        l = m;
      else
        r = m;
    }
    cout << l << endl;
  }
  return 0;
}

