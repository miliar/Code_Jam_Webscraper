#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
  int T;

  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    int N, X;
    cin >> N >> X;
    vector<int> S;
    for (int i = 0; i < N; i++) {
      int x;
      cin >> x;
      S.push_back(x);
    }
    sort(S.begin(), S.end());

    int used = 0;
    int discs = 0;
    while (used < N) {
      int x = X;
      int y = 0;

      discs++;
      for (auto i = S.rbegin(); i != S.rend(); i++) {
        if (*i && *i <= x) {
          x -= *i;
          *i = 0;
          used++;
          y++;
          if (y == 2) break;
        }
      }
    }

    cout << "Case #" << cas << ": " << discs << endl;
  }

  return 0;
}
