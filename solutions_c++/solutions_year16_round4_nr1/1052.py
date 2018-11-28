#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int) (a).size())

int n;
int gr, gp, gs;

string coba(int w, int d) {
  if (d == n) {
    if (w == 0) {
      gr--;
      return "R";
    } else if (w == 1) {
      gp--;
      return "P";
    } else if (w == 2) {
      gs--;
      return "S";
    }
    assert(false);
  }
  string r1, r2;
  if (w == 0) {
    r1 = coba(0, d + 1);
    r2 = coba(2, d + 1);
  } else if (w == 1) {
    r1 = coba(1, d + 1);
    r2 = coba(0, d + 1);
  } else if (w == 2) {
    r1 = coba(2, d + 1);
    r2 = coba(1, d + 1);
  }
  if (r1 > r2) {
    swap(r1, r2);
  }
  return r1 + r2;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    int r, p, s;
    cin >> n >> r >> p >> s;
    gr = r;
    gp = p;
    gs = s;
    string a = coba(0, 0);
    if (gr < 0 || gp < 0 || gs < 0) {
      a = "Z";
    }
    gr = r;
    gp = p;
    gs = s;
    string b = coba(1, 0);
    if (gr < 0 || gp < 0 || gs < 0) {
      b = "Z";
    }
    gr = r;
    gp = p;
    gs = s;
    string c = coba(2, 0);
    if (gr < 0 || gp < 0 || gs < 0) {
      c = "Z";
    }
    string ans = min(a, min(b, c));
    static int caseNo = 1;
    printf("Case #%d: %s\n", caseNo++, ans == "Z" ? "IMPOSSIBLE" : ans.c_str());
  }
  return 0;
}

