// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

const int convert[4][4] = {{0, 1, 2, 3},
                           {1, 0, 3, 2},
                           {2, 3, 0, 1},
                           {3, 2, 1, 0}};

const int sign[4][4] = {{1, 1, 1, 1},
                        {1,-1, 1,-1},
                        {1,-1,-1, 1},
                        {1, 1,-1,-1}};

int getCode(char q) {
  assert(q == '1' || ('i' <= q && q <= 'k'));
  return q == '1' ? 0 : (q - 'i' + 1);
}

void forward(pii &p, char q) {
  int qq = getCode(q);
  p.second *= sign[p.first][qq];
  p.first = convert[p.first][qq];
}

void backward(char p, pii &q) {
  int pp = getCode(p);
  q.second *= sign[pp][q.first];
  q.first = convert[pp][q.first];
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    long long x;
    cin >> n >> x;
    string s;
    cin >> s;
    pii whole = {0, 1};
    for (char c : s) {
      forward(whole, c);
    }
    if (whole.first == 0) {
      if (whole.second == 1 || (whole.second == -1 && x % 2 == 0)) {
        cout << "Case #" << t << ": NO" << endl;
        continue;
      }
    } else {
      if (x % 2 != 0 || (x % 2 == 0 && (x / 2) % 2 == 0)) {
        cout << "Case #" << t << ": NO" << endl;
        continue;
      }
    }
    int limit = min(1LL * n * x, 8LL * n);
    long long L = -1, R = -1;
    {
      pii cur = {0, 1};
      for (int i = 0; i < limit; i++) {
        forward(cur, s[i % n]);
        if (cur.first == 1 && cur.second == 1) {
          L = i;
          break;
        }
      }
    }
    {
      pii cur = {0, 1};
      for (int i = 0; i < limit; i++) {
        backward(s[n - 1 - (i % n)], cur);
        if (cur.first == 3 && cur.second == 1) {
          R = 1LL * n * x - 1 - i;
          break;
        }
      }
    }
    if (L != -1 && R != -1 && L < R) {
      cout << "Case #" << t << ": YES" << endl;
    } else {
      cout << "Case #" << t << ": NO" << endl;
    }
  }
  return 0;
}

