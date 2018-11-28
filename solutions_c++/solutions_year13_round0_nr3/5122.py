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
#define eprintf(...) {fprintf(stderr, __VA_ARGS__);fflush(stderr);}

#define eps 1e-12

#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair(a,b) 
#define forn(i,n) for(int i=0;i<(int)n;i++)
#ifdef DEBUG
#define deb(x) cerr<<#x<<'='<<x<<endl
#else
#define deb(x) 
#endif
typedef long long ll;

using namespace std;

bool good(ll a){
  static char str[200];
  int len = 0;
  while(a){
    str[len] = a % 10;
    a/=10;
    len++;
  }
  for(int i = 0; i < len;i++)
    if(str[i] != str[len - 1 - i])
      return false;
  return true;
}
int main()         
{
  #define taskname ""
  #ifdef DEBUG
  assert(freopen(taskname"in","r",stdin));
  assert(freopen(taskname"out","w",stdout));
  #endif
  int _;
  scanf("%d",&_);
  vector<ll> mas;
  forn(i, 1e7 + 1)
    if(good(i) && good(i*((ll)i))){
      mas.push_back(i*((ll)i));
      deb(i*((ll)i));
    }
  forn(__,_){
    printf("Case #%d: ",__ + 1);
    ll a,b;
    cin>>a>>b;
    printf("%d\n",upper_bound(mas.begin(),mas.end(),b) - lower_bound(mas.begin(),mas.end(),a));
  }
  return 0;
}

