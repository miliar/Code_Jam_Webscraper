#include <iostream>
#include <fstream>


using namespace std;

int main(int argc, char* argv[]) {
  if (argc < 2) return 0;

  ifstream ifs(argv[1]);

  int t;
  ifs >> t;

  for (int i = 0; i < t; ++i) {
    int K, C, S;
    ifs >> K >> C >> S;

    cout << "Case #" << i+1 << ":";
    if (K != S) {
      cout << " IMPOSSIBLE" << endl;
      continue;
    }

    for (int j = 0; j < K; ++j) {
      cout << " " << j+1;
    }
    cout << endl;

  }

  return 0;
}
