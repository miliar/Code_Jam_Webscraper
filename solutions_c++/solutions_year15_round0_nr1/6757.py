#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main(int argc, char* args[]) {
  if (argc != 2) {
    cout << "Usage: " << args[0] << " [file]" << endl;
  }

  ifstream fin(args[1]);

  if (!fin.is_open()) {
    cout << "File: " << args[1] << " failed to open" << endl;
    exit(1);
  }

  int N;
  fin >> N;

  for (int t = 0; t < N; ++t) {
    int max_shy;
    fin >> max_shy;
    string levels;
    fin >> levels;

    int count = levels[0] - '0';
    int answer = 0;
    cerr << levels << endl;
    for (int i = 1; i < max_shy + 1; i++) {
      if (i > count) {
        ++answer;
        ++count;
      }
      cerr << i << " " << levels[i] << count << answer << endl;
      count += levels[i] - '0';
    }
    
    cout << "Case #" << t + 1 << ": " << answer << endl;
  }

  fin.close();
}
