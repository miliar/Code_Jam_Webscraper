#include <iostream>
#include <vector>
#include <string>
using namespace std;
bool work(int r, int c, int m, vector<string> *ans, bool *need_revert) {
  if (r > c) {
    *need_revert = true;
    int ch = r;
    r = c;
    c = ch;
  }
  if (m == 1) {
    string s(c, '*');
    ans->resize(r, s);
    (*ans)[0][0] = 'c';
    return true;
  }
  // if (m == r * c) {
  //   for (int i = 0; i < r; ++i) {
  //     string s(c, '.');
  //     ans->push_back(s);
  //   }
  //   (*ans)[0] = string(c - 1, '.') + "c";
  //   return true;
  // }
  if (r == 1) {
    ans->push_back("c" + string(m - 1, '.') + string(c - m, '*'));
    return true;
  }
  if (r == 2) {
    if (m % 2 == 0 && m > 2) {
      string s = string(m / 2, '.') + string(c - m / 2, '*');
      ans->push_back(s);
      s[0] = 'c';
      ans->push_back(s);
      return true;
    } else {
      return false;
    }
  }
  if (m == 2 || m == 3 || m == 5 || m == 7) return false;
  ans->resize(r, "");
  for (int i = 0; i < c && m > 0; ++i) {
    if (m == 3) break;
    (*ans)[0].push_back('.');
    (*ans)[1].push_back('.');
    m -= 2;
  }
  for (int i = 2; i < r && m; ++i) {
    if (m <= c) {
      (*ans)[i] = string(m, '.');
      m = 0;
      break;
    }
    if (m == c + 1) {
      (*ans)[i] = string(c - 1, '.');
      m = 2;
    } else {
      (*ans)[i] = string(c, '.');
      m -= c;
    }
  }
  (*ans)[0][0] = 'c';
  for (int i = 0; i < r; ++i) {
    while ((*ans)[i].size() < c) (*ans)[i].push_back('*');
  }
  return true;
}
int main() {
  int tc;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    int r, c, m;
    scanf("%d%d%d", &r, &c, &m);
    bool need_revert = false;
    vector<string> ans;
    bool possible = work(r, c, r * c - m, &ans, &need_revert);
    printf("Case #%d:\n", cas);
    if (possible) {
      if (need_revert) {
        for (int i = 0; i < ans[0].size(); ++i) {
          for (int j = 0; j < ans.size(); ++j) {
            printf("%c", ans[j][i]);
          }
          printf("\n");
        }
      } else {
        for (int i = 0; i < ans.size(); ++i) {
          printf("%s\n", ans[i].c_str());
        }
      }
    } else {
      printf("Impossible\n");
    }
  }
  return 0;
}
