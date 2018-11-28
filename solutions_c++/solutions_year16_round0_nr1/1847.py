#include <algorithm>
#include <bitset>
#include <cmath>
#include <fstream>
#include <iostream>
#include <queue>
#include <stack>
#include <string.h>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
ifstream fin ("large.in");
ofstream fout ("large.out");
const int INF = 0x3f3f3f3f;

int T, N;

int main() {
  fin >> T;
  for(int t = 1;  t<= T; ++t) {
    fin >> N;
    fout << "Case #" << t << ": ";
    if (N == 0)
      fout << "INSOMNIA";
    else {
      int d[10], c = 10;
      for(int i = 0; i < 10; ++i)
        d[i] = 0;
      int num = N;
      do {
        int x = num, y;
        while(x) {
          y = x % 10;
          x /= 10;
          if (d[y] == 0) {
            ++d[y];
            --c;
          }
        }
      } while (c > 0 && (num += N));
      fout << num;
    }
    fout << "\n";
  }

  return 0;
}