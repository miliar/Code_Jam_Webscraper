#include <cassert>
#include <cstdio>
#include <map>
#include <set>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector <string> v[101];
vector <string> vv[121];

char s[121];

void gen1 (int i, int x, int pos) {
  if (pos == (i >> 1)) {
    for (int j = 0; j <= 2; j++) {
      if (j * j + 2 * x < 10) {
        s[pos] = j + '0';
        for (int t = 0; t < pos; t++)
          s[i - t - 1] = s[t];
        v[i].push_back (s);
      }
    }
    return;
  }
  s[pos] = '0';
  gen1 (i, x, pos + 1);
  if (x < 4) {
    s[pos] = '1';
    gen1 (i, x + 1, pos + 1);
  }
}

void gen2 (int i, int x, int pos) {
  if (pos == (i >> 1)) {
    for (int t = 0; t < pos; t++)
      s[i - t - 1] = s[t];
    v[i].push_back (s);
    return;
  }

  s[pos] = '0';
  gen2 (i, x, pos + 1);
  if (x < 4) {
    s[pos] = '1';
    gen2 (i, x + 1, pos + 1);
  }
}

int main(void) {
  int tn, nt;
  scanf("%d", &nt);

  v[1].push_back ("1");
  v[1].push_back ("2");
  v[1].push_back ("3");

  string left = "2";
  string right = "2";
  for (int i = 2; i <= 50; i++) {
    s[0] = '1';
    if (i & 1) {
      gen1 (i, 1, 1);

      v[i].push_back (left + "0" + right);
      v[i].push_back (left + "1" + right);
      left += "0";
      right = "0" + right;
    } else {
      gen2 (i, 1, 1);

      v[i].push_back (left + right);
    }
  }

  int cnt = 0;
  for (int i = 1; i <= 50; i++) {
    for (int j = 0; j < (int)v[i].size(); j++) {
      string ss = v[i][j];
      for (int x = 0; x < i; x++) {
        ss[x] -= '0';
      }

      memset (s, 0, sizeof (s));
      for (int x = 0; x < i; x++) {
        for (int y = 0; y < i; y++) {
          s[x + y] += ss[x] * ss[y];
        }
      }
      for (int x = 0; x < i + i - 1; x++) {
        assert (s[x] <= 9);
        s[x] += '0';
      }
      s[i + i - 1] = 0;
      vv[i + i - 1].push_back (s);

      cnt++;
//      cerr << ++cnt << " " << v[i][j] << " " << vv[i + i - 1][j] << endl;
    }
  }
  cerr << cnt << " " << vv[99].size() << " " << vv[13].size() << endl;

  for (tn=1; tn<=nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    string a, b;
    cin >> a >> b;

    int aa = a.size(), bb = b.size();
    int res = 0;
    for (int i = 1; i <= 99; i += 2) {
      if (aa < i && i < bb) {
        res += vv[i].size();
      } else if (aa == i || i == bb) {
        for (int j = 0; j < (int)vv[i].size(); j++) {
          res += ((aa < i || (aa == i && a <= vv[i][j])) && (i < bb || (i == bb && vv[i][j] <= b)));
        }
      }
    }

    printf ("%d\n", res);
  }

  return 0;
}
