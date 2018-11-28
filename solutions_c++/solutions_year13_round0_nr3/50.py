#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>
#include <iomanip>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

char buf[11000];
vector<string> a;

/* used this to generate numbers.txt
vector<string> v[1100];
int a[110], c[110], ll;

bool check(string& s) {
  int n = (int)s.size();

  int sum = 0;
  forn(i, n) {
    a[i] = s[i] - '0';
    sum += a[i] * a[i];
    if (sum > 10)
      return false;
  }

  memset(c, 0, sizeof(c));

  n++;
  forn(i, n) {
    int carry = 0;
    forn(j, n) {
      c[i + j] = c[i + j] + a[i] * a[j] + carry;
      carry = c[i + j] / 10;
      c[i + j] %= 10;
    }
  }

  int len = 110;
  while (c[len - 1] == 0)
    len--;

  forn(i, len)
    if (c[i] != c[len - 1 - i])
      return false;

  ll = len;

  return true;
}

void gen() {
  vector<string> a;

  for (int len = 1; 2 * len - 1 < 100; len++) {
    cerr << len << ' ' << a.size() << ' ' << clock() << endl;
    int half = len / 2;

    forn(msk, 1 << half) {
      string s;
      forn(i, half)
        if (msk & (1 << i))
          s += "1";
        else
          s += "0";

      if (s[0] == '0')
        s[0] = '2';

      if (len & 1)
        forn(i, 3) {
          string res = s + char('0' + i);
          reverse(all(s));
          res += s;
          reverse(all(s));

          if (check(res)) {
            forn(i, ll)
              printf("%d", c[i]);
            puts("");
            a.pb(res);
          }
        }
      else {
        string res = s;
        reverse(all(s));
        res += s;

        if (check(res)) {
          forn(i, ll)
            printf("%d", c[i]);
          puts("");
          a.pb(res);
        }
      }
    }
  }
}
*/

void reada() {
  freopen("numbers.txt", "rt", stdin);
  while (scanf("%s", buf) == 1) {
    a.pb(buf);
  }
  fclose(stdin);
}

int cmp(const string& s1, const string& s2) {
  if (s1 == s2)
    return 0;
  if (s1.size() != s2.size())
    return s1.size() < s2.size() ? -1 : +1;

  return s1 < s2 ? -1 : +1;
}

int main() {
  reada();

  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int tt;
  cin >> tt;
  for (int test = 1; test <= tt; test++) {
    if (test % 10 == 0)
      cerr << test << endl;
    string l, r;
    cin >> l >> r;

    if (cmp(l, r) > 0)
      throw;

    int ans = 0;
    forn(i, a.size())
      if (cmp(l, a[i]) <= 0 && cmp(a[i], r) <= 0)
        ans++;

    printf("Case #%d: %d\n", test, ans);
  }
  
  return 0;
}