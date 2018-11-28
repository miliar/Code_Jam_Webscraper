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
  ifstream cin("/Users/Zetilov/Downloads/D-small-attempt0.in.txt");
  ofstream fout("/Users/Zetilov/ClionProjects/untitled/output.txt");
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  fout.setf(ios_base::fixed);
  fout.precision(28);

  int tst;
  cin >> tst;
  for (int cs = 1; cs <= tst; ++cs) {
    fout << "Case #" << cs << ": ";

    cout << cs << endl;
    int k, c, s;
    cin >> k >> c >> s;
    for (int i = 1; i <= s; ++i) {
      fout << i << ' ';
    }
    fout << '\n';
  }
  return 0;
}