#include <vector>
#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int convert_char(char c) {
  if (c == 'i') return 1;
  if (c == 'j') return 2;
  if (c == 'k') return 3;
}

int main() {
  vector<vector<int>> v ({{0, 1, 2, 3, 4, 5, 6, 7},
                          {1, 4, 3, 6, 5, 0, 7, 2},
                          {2, 7, 4, 1, 6, 3, 0, 5},
                          {3, 2, 5, 4, 7, 6, 1, 0},
                          {4, 5, 6, 7, 0, 1, 2, 3},
                          {5, 0, 7, 2, 1, 4, 3, 6},
                          {6, 3, 0, 5, 2, 7, 4, 1},
                          {7, 6, 1, 0, 3, 2, 5, 4}});

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tt;
  scanf("%d", &tt);
  for (int qq (1); qq <= tt; ++qq) {
    printf("Case #%d: ", qq);
    unsigned long long l, t;
    scanf("%llu", &t);
    scanf("%llu", &l);
    string s;
    cin >> s;

    int currl = 0, currr = 0;
    bool flag (false);
    vector<int> vec (l * t, 0);
    vector<int> veb (l * t, 0);
    int tempera (0), bempera (0);
    for (unsigned long long i (0); i < vec.size(); ++i) {
        vec[i] = v[tempera][convert_char(s[i % t])];
        tempera = vec[i];
        veb[veb.size() - 1 - i] = v[convert_char(s[(veb.size() - 1 - i) % t])][bempera];
        bempera = veb[veb.size() - 1 - i];
    }
    unsigned long long i (0);
    while (true) {
      if (flag) break;
      while (vec[i] != 1 && i < l * t) {
        ++i;
      }
      if (i >= l * t) {
        printf("NO\n");
        break;
      }
      unsigned long long k (l * t - 1);
      while (k > i) {
        while (veb[k] != 3 && k > i) {
          --k;
        }
        if (k <= i) {
          break;
        }

        if (vec[k-1] == 3) {
          printf("YES\n");
          flag = true;
          break;
        }
        --k;
      }
    ++i;
    }
  }
  return 0;
}
