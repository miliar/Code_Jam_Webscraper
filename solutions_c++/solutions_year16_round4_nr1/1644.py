#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef vector<vector<string> > V;

int T, N, R, P, S;
V buf;

void input() {
  cin >> N >> R >> P >> S;
}

void prepare() {
  buf.resize(13);
  for (int i = 0; i < 13; ++i) {
    buf[i].resize(3);
  }
  buf[0][0] = "R";
  buf[0][1] = "P";
  buf[0][2] = "S";
  buf[1][0] = "RS";
  buf[1][1] = "PR";
  buf[1][2] = "PS";
  for (int i = 2; i < 12; ++i) {
    for (int j = 0; j < 3; ++j) {
      string a = buf[i - 1][j].substr(0, (1<<(i - 2)));
      string b = buf[i - 1][j].substr((1<<(i-2)), (1<<(i-2)));
      string aa, bb;
      for (int k = 0; k < 3; ++k) {
        if (a == buf[i - 2][k]) {
          aa = buf[i - 1][k];
        }
        if (b == buf[i - 2][k]) {
          bb = buf[i - 1][k];
        }
      }
      if (aa < bb) {
        buf[i][j] = aa + bb;
      } else {
        buf[i][j] = bb + aa;
      }
    }
  }
}

string expand(string s) {
  string t;
  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == 'R') {
      t += "RS";
    } else if (s[i] == 'S') {
      t += "PS";
    } else if (s[i] == 'P') {
      t += "PR";
    }
  }
  return t;
}

void solve() {
  int m = N;
  int rr = R;
  int pp = P;
  int ss = S;
  bool possible = true;
  while (m > 0) {
    --m;
    int t = (1 << m);
    if (rr > t || pp > t || ss > t) {
      possible = false;
      break;
    }
    int rr_t = t - pp;
    int pp_t = t - ss;
    int ss_t = t - rr;
    rr = rr_t;
    pp = pp_t;
    ss = ss_t;
  }
  if (!possible) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    string ans;
    if (rr == 1) {
      cout << buf[N][0] << endl;
    } else if (pp == 1) {
      cout << buf[N][1] << endl;
    } else {
      cout << buf[N][2] << endl;
    }
  }
}

int main() {
  prepare();

  cin >> T;
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << i + 1 << ": ";
    input();
    solve();
  }
}
