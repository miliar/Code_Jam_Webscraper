#include<bits/stdc++.h>
using namespace std;

const int N = 1<<10;

int op(int n, int k) {
  n ^= (1<<k) - 1;
  for (int i = 0, j = k -1; i < j; i++, j--) {
    int ai = (n&(1<<i))>>i,
        aj = (n&(1<<j))>>j;
    n -= ai << i;
    n -= aj << j;
    n += ai << j;
    n += aj << i;
  }
  return n;
}

void testcase(int t) {
  string s;
  cin >> s;
  int n = s.length();
  int source = 0;
  for (int i = 0; i < n; i++)
    if (s[i] == '-')
      source += 1<< i;
  int d[N];
  fill(d, d+N, -1);
  d[source] = 0;
  queue<int> q;
  for(q.push(source); !q.empty(); q.pop()) {
    int akt = q.front();
    for (int k =1; k <= n; k++) {
      int nb = op(akt, k);
      if (d[nb] == -1) {
        d[nb] = d[akt] + 1;
        q.push(nb);
      }
    }
  }

  printf("Case #%d: %d\n", t, d[0]);
}

int main() {
  int z;
  cin >> z;
  for (int i = 1; i <=z; i++)
    testcase(i);
}
