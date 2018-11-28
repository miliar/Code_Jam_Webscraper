#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iomanip>

using namespace std;

const int M_MAX = 7;
const int N_MAX = 120;
string cool[M_MAX];
int N, M;
char letters[N_MAX];

vector<int> children[N_MAX];
int parents[N_MAX][10];

bool is_substr(string a, string b) {
  // TODO: faster?
  return b.find(a) != string::npos;
}

int get_top(int x, bool avail[]) {
  assert(avail[x]);
  int next;
  for (int i = 7; i >= 0; i--) {
    next = parents[x][i];
    if (next != -1 && avail[next])
      break;
  }
  if (next == -1 || (!avail[next]))
    return x;
  return get_top(next, avail);
}

void simulate(bool success[]) {
  bool avail[N_MAX];
  for (int i = 0; i < N; i++)
    avail[i] = true;

  int guys_left[N_MAX];
  int left_pos[N_MAX];
  for (int i = 0; i < N; i++) {
    guys_left[i] = i;
    left_pos[i] = i;
  }

  char s[N_MAX];
  for (int k = N; k > 0; k--) {
    for (int i = 0; i < k; i++)
      assert(avail[guys_left[i]]);

    int x = guys_left[rand() % k];
    int choice = get_top(x, avail);
    // cout << "choice is " << choice << endl;
    s[N - k] = letters[choice];
    avail[choice] = false;

    int temp = guys_left[k - 1];
    guys_left[k - 1] = choice;
    guys_left[left_pos[choice]] = temp;
    left_pos[temp] = left_pos[choice];
    left_pos[choice] = k - 1;
  }

  s[N] = '\0';
  string S(s);
  for (int i = 0; i < M; i++)
    success[i] = is_substr(cool[i], S);
}

void init() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    children[i].clear();
  }
  for (int i = 0; i < N; i++) {
    int pre; cin >> pre;
    parents[i][0] = pre - 1;
  }
  for (int i = 1; i <= 7; i++) {
    for (int j = 0; j < N; j++) {
      int p = parents[j][i - 1];
      if (p != -1)
        p = parents[p][i - 1];
      parents[j][i] = p;
    }
  }

  /*
  bool temp[N_MAX];
  for (int i = 0; i < N; i++)
    temp[i] = true;
  cout << get_top(0, temp) << "\n";
  cout << get_top(1, temp) << "\n";
  */

  for (int i = 0; i < N; i++)
    cin >> letters[i];

  cin >> M;
  for (int i = 0; i < M; i++)
    cin >> cool[i];
}

void solve_case(int t) {
  init();

  int num_trials = 100000;
  int success[M_MAX];
  for (int i = 0; i < M; i++)
    success[i] = 0;
  for (int i = 0; i < num_trials; i++) {
    // cout << "trial " << i << endl;
    bool s[M_MAX];
    simulate(s);
    for (int j = 0; j < M; j++) {
      if (s[j])
        success[j]++;
    }
  }

  cout << "Case #" << t << ":";
  cout << fixed << setprecision(4);
  for (int i = 0; i < M; i++) {
    assert(success[i] <= num_trials);
    cout << " " << success[i] / ((double) num_trials);
  }
  cout << "\n";
}

int main() {
  srand(time(NULL));

  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}




/*
int _tree_size[N_MAX];
int tree_size(int x) {
  if (_tree_size[x] == -1) {
    int tot = 1;
    for (int i = 0; i < children[x].size(); i++) {
      int child = children[x][i];
      tot += tree_size(child);
    }
    _tree_size[x] = tot;
  }
  return _tree_size[x];
}
*/
