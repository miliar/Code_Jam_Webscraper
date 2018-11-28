#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define maxN 100

bool compare(int i, int j) {
  return i < j;
}

int solve(vector<int> &motes, int A, int i, int N) {
  if (i == N)
    return 0;
  if (A > motes[i])
    return solve(motes, A+motes[i], i+1, N);
  if (A == 1)
    return N-i;
  if (2*A-1 > motes[i])
    return 1+solve(motes, 2*A-1+motes[i], i+1, N);

  // add one more
  int t1 = 1+solve(motes, 2*A-1, i, N);
  // delete one
  int t2 = 1+solve(motes, A, i, N-1);
  return (t1 < t2) ? t1 : t2;
}

void onecase() {
  int A, N;
  scanf("%d %d", &A, &N);
  vector<int> motes;
  int size;
  for (int i = 0; i < N; i++) {
    scanf("%d", &size);
    motes.push_back(size);
  }
  sort(motes.begin(), motes.end(), compare);
  int count = solve(motes, A, 0, N);
  static int t;
  printf("Case #%d: %d\n", ++t, count);
}

int main() {
//  string fname = "data", in = fname+".in", out = fname+".out";
//  freopen(in.c_str(), "r", stdin);
//  freopen(out.c_str(), "w", stdout);
  int t;
  scanf("%d", &t);
  while (t--) onecase();
}
