#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <list>
using namespace std;

#define system(x) {};
#define cout fout

int main() {
  int cases = 0;
  ifstream fin("i.in");
  ofstream fout("o.out");
  fin >> cases;
  for (int i = 1; i <= cases; ++i) {
    unsigned long long one = 0;
    unsigned long long two = 0;
    int N;
    fin >> N;
    int largestDiff = 0;
    int firstDec = 1000;
    vector<int> m(N);
    for (int j = 0; j < N; ++j) fin >> m[j];
    for (int j = 1; j < N; ++j) {
      if (m[j-1] > m[j]) {
        one += m[j-1] - m[j];
        if (m[j-1] - m[j] > largestDiff) {
          largestDiff = m[j-1] - m[j];
        }
      }
    }
    for (int j = 0; j < N - 1; ++j) {
      two += min(m[j], largestDiff);
    }
    if (largestDiff == 0) two = 0;
    cout << "Case #" << i << ": " << one << " " << two << endl;
  }
  system("pause");
}

