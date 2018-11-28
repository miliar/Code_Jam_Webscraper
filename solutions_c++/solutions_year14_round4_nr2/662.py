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

            int n; cin >> n;
            int a[n];
            for (int i = 0; i < n; i++) cin >> a[i];

            int ans = 0;
            int start = 0, end = n - 1;
            while (start < end)
            {
                  int mini = 0x3f3f3f3f, idx = -1;
                  for (int i = start; i <= end; i++)
                        if (a[i] < mini)
                        {
                              mini = a[i];
                              idx = i;
                        }

                  ans += min(idx - start, end - idx);

                  if (idx - start < end - idx)
                  {

                        for (int i = idx; i > start; i--) swap(a[i], a[i-1]);
                        start++;
                  }
                  else
                  {
                        for (int i = idx; i < end; i++) swap(a[i], a[i+1]);
                        end--;
                  }
            }

            cout << "Case #" << tt << ": " << ans << "\n";
      }
      return 0;
}