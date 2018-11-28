#include <iostream>
#include <string>
#include <sstream>

using namespace std;

// dummy solution only for small set

// S - graduate students;
// C - complexity
// K - original sequence of K tiles
// small set -> K == S

void solve(int K, int C, int S, int case_num) {
  stringstream result;

  result << "Case #" << case_num << ": ";
  for (int i=1; i<=K; i++) {
    result << i << " ";
  }

  string res = result.str();

  res = res.substr(0, res.size()-1);

  cout << res << endl;
}

int main() {
  int T;
  cin >> T;

  for (int i=0; i<T; i++) {
    int K;
    int C;
    int S;

    cin >> K >> C >> S;

    solve(K, C, S, i+1);
  }

  return 0;
}
