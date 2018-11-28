#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <fstream>
#include <thread>
#include <assert.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <iomanip>
#include <forward_list>

using namespace std;

long long diff(long long a, long long b) {
  if (a > b) {
    return a - b;
  }
  return b - a;
}

int main(int argc, const char * argv[]) {
  freopen("/Users/efimovmichael/Downloads/al.txt","r",stdin);
  freopen("/Users/efimovmichael/a.out","w",stdout);

  int t;
  cin >> t;
  for (int xx = 1; xx <= t; ++xx) {
    string s;
    cin >> s;
    int k;
    cin >> k;
    int c = 0;
    for (int i = 0; i < s.size(); ++i) {
      int j = i + k;
      if (s[i] == '-') {
        if (j > s.size()) {
          cout << "Case #" << xx << ": " << "IMPOSSIBLE" << endl;
          c = -1;
          break;
        }
        ++c;
        for (int x = i; x < j; ++x) {
          if (s[x] == '-') {
            s[x] = '+';
          } else {
            s[x] = '-';
          }
        }
      }
    }
    if (c != -1) {
      cout << "Case #" << xx << ": " << c << endl;
    }
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
