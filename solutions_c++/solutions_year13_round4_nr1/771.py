#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<LL,LL>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;
#define PIP pair<pair<LL, LL>, LL>
#define MOD 1000002013
vector<PIP> arr;
LL N, M;

LL get_cost(LL dist) {
  return ((N*dist) - (dist*(dist-1))/2)%MOD;
}

bool ticketcomp(PII a, PII b) {
  if (a.first < b.first) {
    return true;
  } else if (a.first > b.first) {
    return false;
  } else if (a.second < b.second) {
    return true;
  }
  return false;
}

bool arrcomp(PIP a, PIP b) {
  if (a.first.first < b.first.first) {
    return true;
  } else if (a.first.first == b.first.first && a.second < b.second) {
    return true;
  }
  return false;
}
LL solve() {
  sort(arr.begin(), arr.end(), arrcomp);
  vector<PII> tickets;
  LL cost = 0;
  FORN(i, arr.size()) {
    PIP t = arr[i];
    //cout<<"one: "<<t.second<<" "<<t.first.first<<" "<<t.first.second<<endl;
    if (t.second == 0) {
      tickets.PB(MP(t.first.first, t.first.second));
    } else {
      LL need_tick = t.first.second;
      while (need_tick > 0) {
        sort(tickets.begin(), tickets.end(), ticketcomp);
        PII x = tickets[tickets.size()-1];
        //cout << "two: "<< need_tick <<" "<<t.second<<" "<<x.first<<" "<<x.second<<endl;
        tickets.pop_back();
        LL got_tick = x.second <= need_tick ? x.second:need_tick;
        //cout <<"got_tick: "<< got_tick<<endl;
        x.second -= got_tick;
        LL dist = t.first.first - x.first;
        //cout<<"dist: "<<dist<<endl;
        cost += (get_cost(dist)*got_tick)%MOD;
        cost %= MOD;
        //cout<<"cost: "<<cost<<endl;
        if (x.second > 0) {
          tickets.PB(x);
        }
        need_tick -= got_tick;
      }
    }
  }
  return cost;
}
int main() {
  int tes;
  GI(tes);
  FORN(t, tes) {
    cin >> N >> M;
    arr.clear();
    LL actual_cost = 0;
    FORN(i, M) {
      LL a, b, c;
      cin >> a >> b >> c;
      LL dist = b-a;
      actual_cost += (get_cost(dist)*c)%MOD;
      actual_cost %= MOD;
      PIP t1 = MP(MP(a, c), 0);
      arr.PB(t1);
      PIP t2 = MP(MP(b, c), 1);
      arr.PB(t2);
    }
    LL ans = solve()%MOD;
    actual_cost %= MOD;
    LL loss = (actual_cost-ans);
    loss = loss < 0?loss+MOD:loss;
    printf("Case #%d: %lld\n", t+1, loss);
  }
}
