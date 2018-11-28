#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <random>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

typedef int64_t i64;
using namespace std;

bool solve(i64 N, i64 L, const vector<vector<char>>& G, const vector<char>& test,
           const vector<char>& first) {
  /*
  char buf[1000];
  for (i64 i = 0; i < test.size(); i++)
    buf[i] = test[i];
  buf[test.size()] = '\0';
  printf("solve: %s\n", buf);
  for (i64 i = 0; i < first.size(); i++)
    buf[i] = first[i];
  buf[first.size()] = '\0';
  printf("\t%s\n", buf);*/
  for (i64 i = 0; i < N; i++) {
    i64 at = 0;
    i64 fat = 0;
    char value = '0';
    for (i64 j = 0; j < L; j++) {
      while (first[fat] != '?') {
        value = first[fat];
        fat++;
      }
      fat++;
      if (value == G[i][j])
        continue;
      while (at < L && test[at] != G[i][j]) {
        at++;
      }
      if (at == L) {
        //printf("\tfail on: %lld %lld\n", i, j);
        return false;
      }
      value = test[at];
      at++;
    }
  }
  //printf("solved\n");
  return true;
}

int main() {
  i64 Z;
  cin >> Z;
  char buf[1000];
  for (i64 T = 1; T <= Z; T++) {
    i64 N, L;
    cin >> N >> L;
    vector<vector<char>> G;
    for (i64 i = 0; i < N; i++) {
      cin >> buf;
      G.push_back(vector<char>(L));
      for (i64 j = 0; j < L ;j++)
        G.back()[j] = buf[j];
    }
    vector<char> B(L);
    cin >> buf;
    for (i64 j = 0; j < L; j++)
      B[j] = buf[j];

#if 0
    for (i64 i = 0; i < N; i++) {
      if (G[i] == B) {
        cout << "MATCHED" << endl;
      }
    }
#endif
    bool ans = false;
    
    vector<char> first;
    for (i64 i = 0; i < L; i++) {
      if (i > 0 && B[i] != B[i-1]) {
        first.push_back('?');
      } else {
        first.push_back(B[i] == '1' ? '0' : '1');
        first.push_back('?');
      }
    }
    for (i64 i = 0; i < L; i++) {
      vector<char> test;
      test.insert(test.end(), B.begin(), B.begin() + i);
      test.insert(test.end(), B.begin() + i + 1, B.end());
      if (test.size() == 0) {
        assert(L == 1);
        test.push_back(B[0] == '1' ? '0' : '1');
      }
      if (solve(N, L, G, test, first)) {
        i64 q = 0;
        for (i64 j = 0; j < first.size(); j++) {
          buf[j] = first[j];
          if (buf[j] == '?')
            q++;
        }
        assert(first.size() > 0);
        assert(test.size() > 0);
        assert(q == L);
        buf[first.size()] = '\0';
        assert(first.size() + test.size() <= 200);
       // cout << L<< " " << first.size() << " " << test.size() << endl;
        printf("Case #%lld: %s", T, buf);
        for (i64 j = 0; j < test.size(); j++)
          buf[j] = test[j];
        buf[test.size()] = '\0';
        printf(" %s\n", buf);
        ans = true;
        break;
      }
    }
    if (!ans) {
      printf("Case #%lld: IMPOSSIBLE\n", T);
    }
  }
  return 0;
}
