#include <iostream>

#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

#include <cmath>
#include <algorithm>

#include <fstream>

using namespace std;

#define M_PI 3.14159265358979323846264338327950288

int main()
{
  ifstream cin("/Users/Zetilov/Downloads/A-large.in.txt");
  ofstream fout("/Users/Zetilov/ClionProjects/untitled/output.txt");
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  fout.setf(ios_base::fixed);
  fout.precision(28);

  int tst;
  cin >> tst;
  for (int cs = 1; cs <= tst; ++cs) {
    fout << "Case #" << cs << ": ";

    int n, cnt = 10;
    cin >> n;
    cout << cs << ' ' << n << endl;
    int c = 0;
    if (n == 0) {
      fout << "INSOMNIA\n";
      continue;
    }
    vector<bool> nus(10, 1);
    while (cnt > 0) {
      c += n;
      int z = c;
      while (z > 0) {
        int d = z % 10;
        cnt -= nus[d];
        nus[d] = 0;
        z /= 10;
      }
    }
    fout << c << '\n';
  }
  return 0;
}