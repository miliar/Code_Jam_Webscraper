#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <vector>
#include <string>

using namespace std;

string next_round(string s) {
  string r = "";

  for(int i = 0; i < (int)s.size(); i += 2) {
    if (s[i] == s[i+1]) return "";
    if (s[i] == 'P') {
      r += (s[i+1] == 'R') ? "P" : "S";
    }
    else if (s[i] == 'R') {
      r += (s[i+1] == 'S') ? "R" : "P";
    }
    else if (s[i] == 'S') {
      r += (s[i+1] == 'P') ? "S" : "R";
    }
  }

  return r;
}

int main() {
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++) {
    int N, R, P, S;
    scanf("%d %d %d %d", &N, &R, &P, &S);

    string s = "";
    for(int i = 0; i < P; i++) s += "P";
    for(int i = 0; i < R; i++) s += "R";
    for(int i = 0; i < S; i++) s += "S";

    int pode = 0;
    do {
      string a, b;
      a = s;
      for(a = s; !pode; a = b) {
        b = next_round(a);
        if (b == "") break;
        if ((int)b.size() == 1) {
          pode = 1;
        }
        a = b;
      }

      if (pode) {
        break;
      }
    } while (next_permutation(s.begin(), s.end()));

    if (!pode) s = "IMPOSSIBLE";
    printf("Case #%d: %s\n", caso, s.c_str());
  }
  return 0;
}

