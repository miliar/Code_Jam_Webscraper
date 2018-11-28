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
  ifstream cin("/Users/Zetilov/Downloads/C-large.in.txt");
  ofstream fout("/Users/Zetilov/ClionProjects/untitled/output.txt");
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  fout.setf(ios_base::fixed);
  fout.precision(28);

  int tst;
  cin >> tst;
  for (int cs = 1; cs <= tst; ++cs) {
    fout << "Case #" << cs << ":\n";

    cout << cs << endl;
    int N, J;
    cin >> N >> J;
    for (int n = 0; n < J; ++n) {
      vector<int> ans;
      int c = n;
      for (int z = 0; z < N / 2 - 2; ++z) {
        int b = c % 2;
        ans.push_back(b);
        ans.push_back(b);
        c /= 2;
      }
      fout << "11";
      for (auto x: ans) {
        fout << x;
      }
      fout << "11 ";
      for (int i = 2; i <= 10; ++i) {
        if (i % 2 == 1) {
          fout << "2 ";
        } else if (i == 2 || i == 8) {
          fout << "3 ";
        } else if (i == 4) {
          fout << "5 ";
        } else if (i == 6) {
          fout << "7 ";
        } else {
          fout << "11";
        }
      }
      fout << '\n';
    }
  }
  return 0;
}