#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>
#include <set>
#include <stack>
#define pb push_back

#define mp make_pair
#define f first
#define s second
#define ll long long

using namespace std;


int solve(string& S) {
  int answer = 0;

  int lastgroup = S[0];

  for (int i = 1; i < S.size(); ) {
    if (S[i] == lastgroup) {
      ++i;
      continue;
    }
    int j = i + 1;
    while(j < S.size() && S[j] == S[i]) {
      ++j;
    }
    if (lastgroup == '-') {
      answer += 1;
    } else {
      answer += 2;
    }
    lastgroup = '+';
    i = j;
  }
  if (lastgroup == '-') {
    answer = 1;
  }
  return answer;
}
int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");

  int T; cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    string S; cin >> S;
    cout << "Case #" << tc << ": " << solve(S) << "\n";
  }
  return 0;
}
