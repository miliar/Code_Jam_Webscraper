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

int numnodes(vector <string>& v)
{
      set <string> s;
      int n = v.size();
      for (int i = 0; i < n; i++)
      {
            int sz = v[i].size();
            for (int j = 0; j <= sz; j++) s.insert(v[i].substr(0, j));
      }
      return s.size();
}

vector <int> decompose(int num, int base)
{
      vector <int> ret;
      while (num)
      {
            ret.push_back(num % base);
            num /= base;
      }
      return ret;
}

int main()
{
      int t; cin >> t;
      for (int tt = 1; tt <= t; tt++)
      {
            cerr << "Executing Case #" << tt << "\n";

            int m, n; cin >> m >> n;
            vector <string> a(m);
            for (int i = 0; i < m; i++) cin >> a[i];

            int MAX = 1;
            for (int i = 0; i < m; i++) MAX *= n;

            int maxsofar = -1, num = 0;
            for (int mask = 0; mask < MAX; mask++)
            {
                  vector <int> digits = decompose(mask, n);
                  digits.resize(m);
                  reverse(digits.begin(), digits.end());

                  vector < vector <string> > v(n);
                  for (int i = 0; i < m; i++) v[digits[i]].push_back(a[i]);

                  int tot = 0;
                  for (int i = 0; i < n; i++) tot += numnodes(v[i]);

                  if (tot > maxsofar)
                  {
                        maxsofar = tot;
                        num = 1;
                  }
                  else if (tot == maxsofar) num++;
            }

            cout << "Case #" << tt << ": " << maxsofar << " " << num << "\n";
      }
      return 0;
}