#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define dbg(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define dbg(fmt, args...)
#endif
#define REPS(i, s, n) for(int (i) = (s); (i) < (int)(n); ++(i))
#define REP(i, n) REPS(i, 0, n)
#define pb push_back
#define pii pair<int, int>
#define pll pair<ll, ll>
#define mp make_pair
#define x first
#define y second
#define INFI 1234567890
#define INFL 1234567890123456789LL
typedef long long ll;

#define P 239

using namespace std;

long long strhash (string &s) {
  unsigned long long h = 0;
  REP(i, (unsigned)s.size()) {
    h = h * P + (ll)s[i];
  }
  return (long long)h;
}

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

int main() {
#ifdef DEBUG
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C.out", "w", stdout);
#endif
    int _test_count;
    cin >> _test_count;
    REP(_test_i, _test_count) {
        dbg("Processing test %d\n", _test_i + 1);
        int n;
        scanf("%d\n", &n);
        // dbg("n = %d\n", n);
        int ans = INFI;
        vector<vector<int> > sets;
        map<ll, int> mp;
        int words_count = 0;
        REP(i, n) {
          string line;
          getline(cin, line);
          vector<string> v;
          split(line, ' ', v);
          int k = sets.size();
          sets.pb(vector<int>());
          REP(j, v.size()) {
            ll hash = strhash(v[j]);
            if (mp.count(hash) == 0) {
              mp[hash] = words_count++;
            }
            sets[k].pb(mp[hash]);
          }
        }
        int *a_orig = (int *)calloc(words_count, sizeof(int));
        REP(i, 2) {
          REP(j, sets[i].size()) {
            a_orig[sets[i][j]] |= (i + 1);
          }
        }
        n -= 2;
        REP(mask, 1 << n) {
          int *a = (int *)calloc(words_count, sizeof(int));
          memcpy (a, a_orig, sizeof(int) * words_count);
          REP(i, n) {
            if (mask & (1 << i)) {
              REP(j, sets[i + 2].size()) {
                a[sets[i + 2][j]] |= 1;
              }
            } else {
              REP(j, sets[i + 2].size()) {
                a[sets[i + 2][j]] |= 2;
              }
            }
          }
          int local_ans = 0;
          REP(i, words_count) {
            local_ans += (a[i] == 3);
          }
          ans = min (ans, local_ans);
          free (a);
        }
        printf("Case #%d: %d\n", _test_i + 1, ans);
    }
    return 0;
}