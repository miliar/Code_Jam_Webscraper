#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
      int t; cin >> t;
      for (int tt = 1; tt <= t; tt++)
      {
            cerr << "Executing Case #" << tt << "\n";

            int n, x; cin >> n >> x;
            int a[n];
            for (int i = 0; i < n; i++) cin >> a[i];
            sort(a, a + n);

            int best = 0x3f3f3f3f;

            int cur = 0;
            bool was[n];
            for (int i = 0; i < n; i++) was[i] = false;
            for (int i = 0; i < n; i++)
                  if (!was[i])
                  {
                        cur++;
                        int nxt = -1;
                        for (int j = i + 1; j < n; j++)
                              if (!was[j] and a[j] + a[i] <= x)
                                    nxt = j;
                        if (nxt >= 0) was[nxt] = true;
                  }
            best = min(best, cur);

            cur = 0;
            for (int i = 0; i < n; i++) was[i] = false;
            for (int i = n - 1; i >= 0; i--)
                  if (!was[i])
                  {
                        cur++;
                        int nxt = -1;
                        for (int j = i - 1; j >= 0; j--)
                              if (!was[j] and a[j] + a[i] <= x)
                              {
                                    nxt = j;
                                    break;
                              }
                        if (nxt >= 0) was[nxt] = true;
                  }
            best = min(best, cur);

            cout << "Case #" << tt << ": " << best << "\n";
      }
      return 0;
}