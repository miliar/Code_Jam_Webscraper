#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>

#define FOR(i, x, y) for(int i=x ; i<y ; ++i)
#define FORD(i, x, y) for(int i=x ; i>=y ; --i)
#define MOD 1000002013

using namespace std;

struct O {
  int o, p;
}o[1010];

struct E {
  int e, p;
}e[1010];

struct original {
  int o, e, p;
}ori[1010];

int n, m;
long long ans;

int cmpO(struct O a, struct O b) {
  return a.o < b.o;
}
int cmpE(struct E a, struct E b) {
  return a.e < b.e;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

  int tt, p;
  scanf("%d", &tt);
  FOR(t, 0, tt) {
    scanf("%d%d", &n, &m);
    FOR(i,0,m) {
      scanf("%d%d%d", &o[i].o, &e[i].e, &p);
      o[i].p = p;
      e[i].p = p;

      ori[i].o = o[i].o;
      ori[i].e = e[i].e;
      ori[i].p = p;
    }

    sort(o, o+m, cmpO);
    sort(e, e+m, cmpE);

    o[m].o = 2000000000;

    long long sumForCheat = 0;
    int left, right, mid;
    FOR(i,0,m) {    // for e b search find min in o
      left = 0; right = m;
      while(left <= right) {
        mid = (left+right)/2;
        if(o[mid].o <= e[i].e && o[mid+1].o > e[i].e) break;
        else if(o[mid].o <= e[i].e) left = mid+1;
        else right = mid-1;
      }
      //printf("b search %d %d\n", i, mid);
      long long distance = 0;
      while(e[i].p > 0) {
        if(e[i].p > o[mid].p) {
          distance = (e[i].e-o[mid].o);
          sumForCheat += ((distance * n - (distance-1)*distance / 2 ) % MOD) * o[mid].p;
          //printf("sum1 = %lld %d %d\n", sumForCheat, o[mid].p, (e[i].e-o[mid].o));
          e[i].p -= o[mid].p;
          o[mid].p = 0;
        }
        else {
          distance = (e[i].e-o[mid].o);
          sumForCheat += ((distance * n - (distance-1)*distance / 2 ) % MOD) * e[i].p;
          //printf("sum2 = %lld %d %d %d %d\n", sumForCheat, e[i].p, (e[i].e-o[mid].o), i, mid);
          o[mid].p -= e[i].p;
          e[i].p = 0;
        }
        mid--;
        sumForCheat %= MOD;
      }
    }
    sumForCheat %= MOD;

    // Normal
    long long normal = 0;
    FOR(i,0,m) {
      long long distance = (ori[i].e-ori[i].o);
      normal +=  ((distance * n - (distance-1)*distance / 2 ) % MOD) * ori[i].p;
      normal %= MOD;
      //printf("%lld\n", normal);
    }
    long long ans = (normal - sumForCheat + MOD) % MOD;
    printf("Case #%d: %lld\n", t+1, ans);
  }

}
