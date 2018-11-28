#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define ls (rt<<1)
#define rs (rt<<1|1)
#define lson l,m,ls
#define rson m+1,r,rs

int main(){
  int T, icase = 1;
  ll a, b;
  scanf("%d", &T);
  while(T--){
    scanf("%lld/%lld", &a, &b);
    ll g = __gcd(a, b);
    a /= g;
    b /= g;
    //cerr<<" a= "<<a<<" b = "<<b<<endl;
    bool ok = true;
    if((b & (b - 1)) != 0) ok = false;
    int ans = 0;
    while(a < b){
      if(b % 2) {
        ok = false;
        break;
      }
      b /= 2LL;
      ans++;
    }
    if(ok)
      printf("Case #%d: %d\n",icase++, ans);
    else
      printf("Case #%d: impossible\n",icase++);
  }
  return 0;
}
