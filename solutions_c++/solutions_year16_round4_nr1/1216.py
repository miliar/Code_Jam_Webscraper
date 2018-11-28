#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
using namespace std;

int loser(int a) {
  if (a == 0) return 2;
  if (a == 1) return 0;
  if (a == 2) return 1;
  return -1;
}
char letter(int a) {
  if (a == 0) return 'R';
  if (a == 1) return 'P';
  if (a == 2) return 'S';
  return 'X';
}


void do_sort(string& s, int a, int b) {
  if (b-a == 2) {
    if (s[a] > s[a+1])
      swap(s[a], s[a+1]);
  }
  else {
    int m = a + (b-a)/2;
    do_sort(s, a, m);
    do_sort(s, m, b);
    int k = m - a;
    for (int j = 0; j < k; j++) {
      if (s[a+j] < s[m+j]) return;
      if (s[a+j] > s[m+j]) {
        for (int jj = 0; jj < k; jj++)
        {
          swap(s[a+jj], s[m+jj]);
        }
        return;
      }
    }
  }
}

string solve(int N, int R, int P, int S) {
  string best;
  for (int w = 0; w < 3; w++) {
    vector<int> x;
    x.push_back(w);
    for (int i = 0; i < N; i++)  {
      vector<int> y;
      for (int a : x) {
        y.push_back(a);
        y.push_back(loser(a));
      }
      y.swap(x);
    }
    vector<int> cnt(3);
    for (int a : x) cnt[a]++;
    if (R != cnt[0] || P != cnt[1] || S != cnt[2]) continue;
    string cur;
    cur.resize(x.size());
    for (int i = 0; i < x.size(); i++) cur[i] = letter(x[i]);
    do_sort(cur, 0, cur.size());
    if (best.empty() || cur > best) best = cur;
  }
  if (best.empty()) best = "IMPOSSIBLE";
  return best;
}

int main(int argc, char* argv[]) {
  uint64_t T;
  fstream f(argv[1]);
  f >> T;
  for (int i = 0; i < T; i++) {
    uint64_t N, R, P, S;
    f >> N >> R >> P >> S;
    cout << "Case #" << (i+1) << ": " << solve(N,R,P,S) << endl;
  } 
  return 0;
}
