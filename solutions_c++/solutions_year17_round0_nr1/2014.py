#include <iostream>
#include <fstream>

#include <stack>
#include <queue>
#include <deque>
#include <vector>

#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>

#include <cmath>

#include <cassert>

#include <algorithm>

using namespace std;


//auto& fin = cin;
//auto& fout = cout;
ifstream fin("///Users/Zetilov/Downloads/A-large.in.txt");
ofstream fout("output.txt");


void solve()
{
  string S;
  fin >> S;
  int k;
  fin >> k;
  int n = S.length();
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    if (S[i] == '-') {
      if (i + k > n) {
        fout << "IMPOSSIBLE";
        return;
      }
      for (int j = 0; j < k; ++j) {
        S[i + j] = (S[i + j] == '+' ? '-' : '+');
      }
      ++ans;
    }
  }
  fout << ans;
}

int main()
{
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  cout.setf(ios_base::fixed);
  cout.precision(28);

  int T;
  fin >> T;
  for (int cs = 1; cs <= T; ++cs) {
    cout << cs << endl;
    fout << "Case #" << cs << ": ";
    solve();
    fout << endl;
  }
  return 0;
}