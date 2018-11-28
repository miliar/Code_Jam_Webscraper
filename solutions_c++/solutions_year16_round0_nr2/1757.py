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
  ifstream cin("/Users/Zetilov/Downloads/B-large.in.txt");
  ofstream fout("/Users/Zetilov/ClionProjects/untitled/output.txt");
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  fout.setf(ios_base::fixed);
  fout.precision(28);

  int tst;
  cin >> tst;
  for (int cs = 1; cs <= tst; ++cs) {
    cout << cs << endl;
    fout << "Case #" << cs << ": ";

    string S;
    cin >> S;
    reverse(S.begin(), S.end());
    char nd = '+';
    int ans = 0;
    for (auto c: S) {
      if (c != nd) {
        ++ans;
        nd = c;
      }
    }
    fout << ans << '\n';
  }
  return 0;
}