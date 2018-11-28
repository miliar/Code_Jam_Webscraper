#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int A;
    int N;
    cin >> A >> N;
    vector<int> mote(N);
    for (int i = 0; i < N; ++i) cin >> mote[i];
    sort(mote.begin(), mote.end());
    int i = 0;
    //vector<int> ops(0);
    int min = N;
    int added = 0;
    if (A <= 1) i = N;
    while (i < N) {
      while (i < N and mote[i] < A) {
        A += mote[i];
        ++i;
      }
      //ops.push_back(added + N - i);
      if (min > added + N - i) min = added + N - i;
      if (i < N) {
        while (mote[i] >= A) {
          A += A-1;
          ++added;
          if (added >= min) {
            A = mote[i] + 1;
            i = N;
          }
        }
      }
    }/*
    int min = 0;
    for (int j = 0; j < ops.size(); ++j)
      if (ops[j] < min) min = ops[j];*/
    cout << "Case #" << cas << ": " << min << endl;
  }
}
