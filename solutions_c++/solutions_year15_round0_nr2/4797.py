#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)

int check;

int dfs(priority_queue<int> q, int depth) {
  int mx = q.top();
  int res = mx;

  if (mx == 1) return 1;
  if (depth == check) return depth;

  // q.pop();
  // q.push(mx / 2);
  // q.push(mx - mx / 2);
  // res = min(res, dfs(q) + 1);

  for (int x = 1; x < mx; x++) {
    priority_queue<int> q2 = q;
    q2.pop();
    q2.push(x);
    q2.push(mx - x);
    res = min(res, dfs(q2, depth + 1) + 1);
  }

  return res;
}

void main2() {
  int D;
  priority_queue<int> q;

  cin >> D;
  REP(i,D) {
    int x;
    cin >> x;
    q.push(x);
  }

  check = q.top();
  cout << dfs(q, 0) << endl;
}

int main() {
  int T;

  scanf("%d\n", &T);
  REP(t,T) {
    printf("Case #%d: ", t + 1);
    main2();
  }

  return 0;
}
