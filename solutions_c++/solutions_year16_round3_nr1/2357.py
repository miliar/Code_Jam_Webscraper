#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

vector<int> P;


int pickMax() {
  int max = 0;
  int maxIndex = -1;
  for (int i = 0; i < P.size(); ++i) {
    if (P[i] > max){
      max = P[i];
      maxIndex = i;
    }
  }
  if (maxIndex != -1) P[maxIndex]--;
  return maxIndex;
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  int t = 0;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    P = vector<int> (N, 0);
    int total = 0;
    for (int i = 0; i < N; ++i) {
      cin >> P[i];
      total += P[i];
    }
    vector<int> indexes = vector<int> (N,0);
    for (int i = 0; i < N; ++i) {
      indexes[i] = i;
    }
    stringstream ss;


    int wi = 0;
    while (total > 0) {
      int party1 = pickMax();
      total--;
      ss << char('A' + party1);
      if (total != 2) {
        int party2 = pickMax();
        if (party2 != -1) {
          ss << char('A' + party2);
          total--;
        }
      }
      ss << " ";
    }

    cout << "Case #" << t << ": " << ss.str() << endl;
  }
  return 0;
}
