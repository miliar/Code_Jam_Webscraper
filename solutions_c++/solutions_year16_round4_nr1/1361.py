#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>

using namespace std;

#define forn(I,N) for (int I=0; I<N; I++)
#define fornd(I,N) for (int I=N-1; I>=0; I--)
#define forab(I,A,B) for (int I=A; I<=B; I++)
#define forabd(I,A,B) for (int I=B; I>=A; I--)
#define FOREACH(I,A) for (__typeof__(A)::iterator I=A.begin(); I<A.end(); I++)
#define pb push_back
#define mp make_pair

typedef long long int ll;

int main() {
  int T;
  cin >> T;

  forn (i, T) {
    int N, R, P, S;
    cin >> N >> R >> P >> S;

    vector<int> r(N + 1), p(N + 1), s(N + 1);
    r[0] = R;
    p[0] = P;
    s[0] = S;

    bool possible = true;
    forab(j, 1, N) {
      r[j] = (r[j - 1] + s[j - 1] - p[j - 1]) / 2;
      p[j] = (p[j - 1] + r[j - 1] - s[j - 1]) / 2;
      s[j] = (s[j - 1] + p[j - 1] - r[j - 1]) / 2;

      if (r[j] < 0 || p[j] < 0 || s[j] < 0) {
        possible = false;
        break;
      }
    }

    cout << "Case #" << i + 1 << ": ";
    if (possible) {
      string str = "";
      if (r.back() == 1) {
        str += "R";
      }
      if (p.back() == 1) {
        str += "P";
      }
      if (s.back() == 1) {
        str += "S";
      }
      forn (j, N) {
        string temp = "";
        forn(k, str.length()) {
          if(str[k] == 'R') {
            temp += "RS";
          } else if(str[k] == 'P') {
            temp += "PR";
          } else {
            temp += "PS";
          }
        }
        str = temp;
      }
      //cout << "str " << str << endl;

      int sz = 1;
      int pw = 1;
      forn (j, N) {
        pw *= 2;
      }
      forn(j, N) {
        string temp = "";
        //cout << sz << endl;
        forn(k, pw / (sz * 2)) {
          if (str.substr(2 * k * sz, sz) <= str.substr((2 * k + 1) * sz, sz)) {
            temp += str.substr(2 * k * sz, sz);
            temp += str.substr((2 * k + 1) * sz, sz);
          } else {
            temp += str.substr((2 * k + 1) * sz, sz);
            temp += str.substr(2 * k * sz, sz);
          }
        }
        //cout << temp << endl;
        str = temp;
        sz *= 2;
      }
      cout << str;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }

  return 0;
}
