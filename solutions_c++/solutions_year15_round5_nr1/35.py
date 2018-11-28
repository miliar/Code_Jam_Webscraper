#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<vector<long long> > vc;
vector<long long> vs;
vector<long long> vpar;
vector<long long> state;
long long cur;
priority_queue<pair<long long, long long> > q;
priority_queue<pair<long long, long long> > q2;

void add(long long x, long long mn, long long mx) {
  if (state[x] != 0) return;
  if (vs[x] > mx) return;
  if (vs[x] < mn) {
    q.push(make_pair(vs[x], x));
    return;
  }
  state[x] = 1;
  cur++;
  q2.push(make_pair(vs[x], x));
  for (long long i = 0; i < vc[x].size(); i++) add(vc[x][i], mn, mx);
}

void sub(long long x) {
  if (state[x] == -1) return;
  if (state[x] == 1) cur--;
  state[x] = -1;
  for (long long i = 0; i < vc[x].size(); i++) sub(vc[x][i]);
}

int main() {
  long long T, N, D, prob=1;
  for (cin >> T; T--;) {
    cin >> N >> D;
    vc = vector<vector<long long> >(N);
    vs = vector<long long>(N);
    vpar = vector<long long>(N);
    long long As, Cs, Rs;
    cin >> vs[0] >> As >> Cs >> Rs;
    for (long long i = 1; i < N; i++) vs[i] = (vs[i-1] * As + Cs) % Rs;
    long long Am, Cm, Rm;
    cin >> vpar[0] >> Am >> Cm >> Rm;
    for (long long i = 1; i < N; i++) vpar[i] = (vpar[i-1] * Am + Cm) % Rm;

    vpar[0] = -1;
    for (long long i = 1; i < N; i++) {
      vpar[i] %= i;
      vc[vpar[i]].push_back(i);
    }

    state = vector<long long>(N, 0);
    cur = 0;
    q = priority_queue<pair<long long, long long> >();
    q2 = priority_queue<pair<long long, long long> >();
    add(0, vs[0], vs[0]+D);
    long long ret = cur;
//for (long long i = 0; i < N; i++) if (state[i] == 1) cout << i << ',' << vs[i] << "  ";
//cout << "cur=" << cur << endl;
    while (!q.empty()) {
      long long goal = q.top().first;
      while (!q2.empty() && q2.top().first > goal+D) {
        sub(q2.top().second);
        q2.pop();
      }
      while (!q.empty() && q.top().first == goal) {
        add(q.top().second, goal, goal+D);
        q.pop();
      }
      ret = max(ret, cur);
//for (long long i = 0; i < N; i++) if (state[i] == 1) cout << i << ',' << vs[i] << "  ";
//cout << "cur=" << cur << endl;
    }

    cout << "Case #" << prob++ << ": " << ret << endl;
  }
}
