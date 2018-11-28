#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

namespace {

const string kImpossible = "IMPOSSIBLE";

string SolveSmall(vector<string> G, string B) {
  if (find(G.begin(), G.end(), B) != G.end()) return kImpossible;
  const int L = B.size();
  string y = "10?";
  string z = "0";
  for (int i = 0; i < L; ++i) y += "10";
  for (int i = 1; i < L; ++i) z += "?";
  return y + " " + z;
}

string Solve(vector<string> G, string B) {
  return SolveSmall(G, B);
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N, L;
    cin >> N >> L;
    vector<string> G(N);
    for (int j = 0; j < N; ++j) cin >> G[j];
    string B;
    cin >> B;
    cout << "Case #" << i << ": " << Solve(G, B) << endl;
  }

  return 0;
}
