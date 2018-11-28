#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

typedef long long LL;
typedef pair<int,int> PI;
const LL mod = 1000002013;

LL legal=0, illegal=0;
int n,m,a,b,c;

vector<PI> ev;
priority_queue<PI> Q;

int ntc;
  
int main() {
  scanf("%d", &ntc);
  for(int ca=1; ca<=ntc; ++ca) {
    while(!Q.empty()) Q.pop();
    ev.clear();
    legal = illegal = 0;
    scanf("%d%d", &n,&m);
    for(int i=0; i<m; ++i) {
      scanf("%d%d%d",&a,&b,&c);
      int l = b-a;
      LL fare = (LL)l*n - (LL)l*(l-1)/2LL;
      fare%=mod;
      fare = (fare*c)%mod;
      legal = (legal+fare)%mod;
      ev.push_back(PI(a,-c)); // - wsiadaja
      ev.push_back(PI(b,c)); // + wysiadaja
    }
    sort(ev.begin(), ev.end());
    for(int i=0; i<ev.size(); ++i) {
      if(ev[i].second < 0) {
        Q.push(PI(ev[i].first, -ev[i].second));
      } else {
        int rem = ev[i].second;
        while(rem) {
          PI cur = Q.top();
          Q.pop();
          int p = min(rem, cur.second);
          int dist = ev[i].first - cur.first;
          LL fare = (LL)dist*n - (LL)dist*(dist-1)/2LL;
          fare %= mod;
          fare=(fare*p)%mod;
          illegal += fare;
          illegal%=mod;
          rem-=p;
          if (p < cur.second) {
            Q.push(PI(cur.first, cur.second-p));
          }
        }
      }
    }
    LL res = (legal + mod - illegal)%mod;
    printf("Case #%d: %d\n", ca, (int)res);
  }
} 


