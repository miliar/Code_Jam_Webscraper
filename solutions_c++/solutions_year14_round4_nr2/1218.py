#include <bits/stdc++.h>
using namespace std;

const int INF = 1<<28;

bool ok(vector<int> &v) {
  int p = max_element(v.begin(), v.end()) - v.begin();
  for(int i = 0; i+1 <= p; ++i) {
    if(v[i] < v[i+1]); else return false;
  }
  for(int i = p; i+1 < v.size(); ++i) {
    if(v[i] > v[i+1]); else return false;
  }
  return true;
}

int bfs(vector<int> &src) {
  map<vector<int>,int> cost;
  queue<vector<int> > que;
  if(ok(src)) return 0;
  que.push(src);
  cost[src] = 0;
  while(que.size()) {
    vector<int> v = que.front();
    que.pop();
    int pc = cost[v];
    for(int i = 0; i+1 < v.size(); ++i) {
      swap(v[i], v[i+1]);
      if(!cost.count(v)) {
        que.push(v);
        cost[v] = pc + 1;
        if(ok(v)) return cost[v];
      }
      swap(v[i], v[i+1]);
    }
  }
  return -1;
}

 int main() {
  for(int Tc, tc = (bool)(cin >> Tc); tc <= Tc; ++tc) {
    cout << "Case #" << tc << ": ";
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; ++i) cin >> A[i];
    cout << bfs(A) << endl;
  }
  return 0;
}
