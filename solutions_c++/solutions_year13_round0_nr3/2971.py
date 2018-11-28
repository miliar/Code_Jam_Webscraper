#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) (int)(x).size()
#define foreach(i,x) for (__typeof(x.begin()) i = x.begin();i!=x.end();++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int maxn = (int)1e5+9;
const int inf = (int)1e9+7;

bool issquare(int a){
  int sa = (int)sqrt(a);
  return sa*sa == a;
}

bool ispal(int a){
  vi num;
  while (a>0){
    num.pb(a%10);
    a/=10;
  }
  bool res = true;
  for (int i=0;i<sz(num)/2;++i)
    if (num[i]!=num[sz(num)-i-1])
      res = false;
  return res;
}

int main(){
  #ifdef LOCAL
  freopen("err","w",stderr);
  #endif
  int t;
  scanf("%d",&t);
  for (int tc=1;tc<=t;++tc){
    int l,r,ans=0;
    scanf("%d%d",&l,&r);
    for (int i=l;i<=r;++i){
      if (issquare(i) && ispal(i) && ispal(sqrt(i))){
        ++ans;
      }
    }
    printf("Case #%d: %d\n",tc,ans);
  }
	return 0;
}

