#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
  {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
      {
        string cakes;
        cin >> cakes;
        vector<int> v;
        for (unsigned i = 0; i < cakes.length(); ++i)
          {
            if (cakes[i] == '+') v.push_back(1);
            else v.push_back(0);
          }
        int r = v.size() - 1;
        int flips = 0;
        while (r >= 0 && v[r] == 1) r--;
        while (r >= 0)
          {
            if (v[0] == 1)
              {
                for (unsigned i = 0; i < v.size(); ++i)
                  {
                    if (v[i] == 0) break;
                    v[i] = 0;
                  }
                flips++;
              }
            else
              {
                for (unsigned i = 0; i <= r; ++i)
                  {
                    v[i] = v[i] == 0 ? 1 : 0;
                  }
                reverse(v.begin(), v.begin()+r+1);
                while (r >= 0 && v[r] == 1) r--;
                flips++;
              }
          }
        cout << "Case #" << t << ": " << flips << "\n";
      }
    return 0;
  }

