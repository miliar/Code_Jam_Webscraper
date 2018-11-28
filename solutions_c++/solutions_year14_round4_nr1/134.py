#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

#include <map>

using namespace std;

const int N_MAX = 10008;
const int X_MAX = 800;
int N, X;
//int by_size[X_MAX];
int sizes[N_MAX];

map<int, int> counts;

void remove_size(int s) {
  counts[s]--;
  if (counts[s] == 0)
    counts.erase(s);
}

void init() {
  //  for (int i = 0; i < X_MAX; i++)
  //    by_size[i] = 0;
  counts.clear();

  cin >> N >> X;
  for (int i = 0; i < N; i++) {
    int size;
    cin >> size;
    sizes[i] = size;
    //by_size[sizes[i]]++;
    if (counts.find(size) == counts.end())
      counts[size] = 0;
    counts[size]++;
  }
  sort(sizes, sizes + N);

}

void solve_case(int t) {
  init();
  int savings = 0;

  for (int i = N - 1; i >= 0; i--) {
    int size = sizes[i];
    if (counts.find(size) == counts.end())
      continue;

    remove_size(size);
    if (counts.size() == 0)
      break;

    map<int, int>::iterator it = counts.upper_bound(X - size);
    if (it == counts.begin())
      continue;

    --it;
    remove_size(it->first);
    savings++;
  }

  cout << "Case #" << t << ": " << N - savings << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
