#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define maxN 1000005

int N, D;
int salary[maxN];
int father[maxN];
vector<int> edges[maxN];

bool in_queues[maxN];
bool dead[maxN];

priority_queue< pii > inside, outside;

/*
int dfs(int u, int now_min, int now_max) {
  if (u == 0) now_min = now_max = salary[u];
//  printf("u %d (father %d) (salary %d), now_min %d, now_max %d\n", u, father[u], salary[u], now_min, now_max);
  now_min = min(now_min, salary[u]);
  now_max = max(now_max, salary[u]);
  if (now_max - now_min > D) return 0;
  int num = 1;
  REP(i, edges[u].size()) {
    num += dfs(edges[u][i], now_min, now_max);
  }
  return num;
}
*/

int fill(int u, int now_min, int now_max) {
  in_queues[u] = true;
  if (salary[u] >= now_min && salary[u] <= now_max) {
    inside.push(mp(salary[u], u));
    dead[u] = true;
    int num = 1;
    REP(i, edges[u].size()) {
      num += fill(edges[u][i], now_min, now_max);
    }
    return num;
  }
  outside.push(mp(salary[u], u));
  return 0;
}

int die(int u) {
  if (in_queues[u]) {
    in_queues[u] = false;
    if (dead[u]) {
      int num = 1;
      REP(i, edges[u].size()) {
        num += die(edges[u][i]);
      }
      return num;
    } else return 0;
  }
  return 0;
}

int main() {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    while (!inside.empty()) inside.pop();
    while (!outside.empty()) outside.pop();
    scanf("%d%d", &N, &D);
    REP(i, N+1) edges[i].clear();
    REP(i, N+1) in_queues[i] = false;
    REP(i, N+1) dead[i] = false;
    long long s0,as,cs;
    int rs;
    scanf("%lld%lld%lld%d", &s0, &as, &cs, &rs);
    int s = s0;
    REP(i, N) {
      salary[i] = s;
//      printf("%d %d\n", i, salary[i]);
      s = ((long long)s * as + cs) % rs;
    }
    long long m0, am, cm;
    int rm;
    scanf("%lld%lld%lld%d", &m0, &am, &cm, &rm);
    int m = m0;
    REP(i, N) {
      if (i) {
        father[i] = (m % i);
//        printf("%d %d\n", i, father[i]);
        edges[father[i]].push_back(i);
      }
      m = ((long long)m * am + cm) % rm;
    }
    int bestnum;
    int nownum = fill(0, salary[0], salary[0] + D);
    bestnum = nownum;
    FORD(d, D, 1) {
//      printf("d %d\n", d);
//      printf("inside %d\n", nownum);
//      auto pq = inside;
//      while(!pq.empty()) {printf("%d %d\n", pq.top().X, pq.top().Y); pq.pop(); }
//      printf("outside\n");
//      pq = outside;
//      while(!pq.empty()) {printf("%d %d\n", pq.top().X, pq.top().Y); pq.pop(); }
      while (true) {
        pii su = inside.top();
        if (!in_queues[su.Y]) { inside.pop(); continue; }
        if (su.X == salary[0] + d) {
          nownum -= die(su.Y);
          inside.pop();
        }
        else break;
      }
      while (!outside.empty()) {
        pii su = outside.top();
        if (!in_queues[su.Y] || dead[su.Y]) { outside.pop(); continue; }
        if (su.X >= salary[0] + d - D) { outside.pop(); continue; }
        if (su.X == salary[0] + d - D - 1) {
          outside.pop();
          nownum += fill(su.Y, salary[0] + d - D - 1, salary[0] + d - 1);
        }
        else break;
      }
      bestnum = max(bestnum, nownum);
    }
    printf("Case #%d: %d\n", t, bestnum);
  }

  return 0;
}
