// mars.ma
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

map<int, int> table =
{
    {4, 2},
    {5, 2},
    {6, 3},
    {7, 3},
    {8, 4},
    {9, 3}
};

int main(void)
{
    int testcase;
    cin >> testcase;
    for (int tc = 1; tc <= testcase; tc++) {
        int D;  cin >> D;
        vector<int> pies(D);
        int bench = 0;
        for (auto& p : pies) { cin >> p; bench = max(bench, p); }
        int result = bench;
        for (int i = (1<<bench) - 1; 0 < i; --i) {
            priority_queue<int> pancakes(pies.begin(), pies.end());
            int remain = i;
            for (int j = 0; j < result; ++j) {
              if ((pancakes.empty()) or (1 == pancakes.top())) {
                  result = min(result, j+1);
                  break;
              }

              bool processed = false;
              if (remain % 2) {
                  // special minute
                  int maximum = pancakes.top();
                  if (0 < table[maximum]) {
                      pancakes.pop();
                      pancakes.push(maximum-table[maximum]);
                      pancakes.push(table[maximum]);
                      processed = true;
                  }
              }

              if (!processed) {
                  // every diner eats one cake
                  vector<int> buffer;
                  while (!pancakes.empty()) {
                      if (1 < pancakes.top()) {
                        buffer.push_back(pancakes.top()-1);
                      }
                      pancakes.pop();
                  }

                  for (const auto& b : buffer) {
                      pancakes.push(b);
                  }
              }
              remain /= 2;
            }
        }

        cout << "Case #" << tc << ": " << result << endl;
    }

    return 0;
}

