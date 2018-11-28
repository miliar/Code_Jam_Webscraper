#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
typedef vector<int> vi;

int tag[128];

int valid_train(string &str)
{
  memset(tag, -1, sizeof(tag));

  int s = str.size();
  for (int i = 0; i < s; i++) {
    int c = str[i];
    if (tag[c] == -1) {
      tag[c] = i; continue;
    }
    if (tag[c] == i - 1) {
      tag[c] = i;
    } else {
      return 0;
    }
  }
  return 1;
}

const long long MAX_P = 1000000007;
int main()
{
  int T = 0;
  scanf("%d", &T);

  for (int Ti = 1; Ti <= T; Ti++) {
    int N;
    scanf("%d", &N);
    vector<string> A;
    for (int i = 1; i <= N; i++) {
      string str;
      cin >> str;
      A.push_back(str);
    }

    vi P(N, 0);
    for (int i = 0; i < N; i++) P[i] = i;

    long long count = 0;
    do {
      string str;
      for (int i = 0; i < N; i++) {
         str += A[P[i]];
      }
      if (valid_train(str)) {
        count++;
        if (count > MAX_P) count = count - MAX_P;
      } else {
      }
    } while (next_permutation(P.begin(), P.end()));

    printf("Case #%d: %lld\n", Ti, count);
  }
  return 0;
}

