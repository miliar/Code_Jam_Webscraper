#include<bits/stdc++.h>
using namespace std;

#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))

const int OO = (int) 2e9;
const double EPS = 1e-9;

int n, t;
vector<string> v;
vector<vector<pair<char, int> > > c;
vector<char> seq;

void conv(string x) {
  vector<pair<char, int> > ret;
  char cur = x[0];
  int f = 1;
  for (int i = 1; i < SZ(x) ; i++) {
    if (x[i] == cur) {
      f++;
    } else {
      ret.push_back(MP(cur, f));
      cur = x[i];
      f = 1;
    }
  }
  ret.push_back(MP(cur, f));
  c.push_back(ret);
}
int main() {

  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    cin >> n;
    v.clear();
    v.resize(n);
    for (int i = 0; i < n; i++)
    cin >> v[i];
    c.clear();
    seq.clear();
    bool bad = 0;
    for (int i = 0; i < n; i++) {
      if (bad)
      break;
      conv(v[i]);
      if (i == 0) {
        for (int j = 0; j < SZ(c[0]); j++)
        seq.push_back(c[0][j].first);
      } else {
        if (SZ(seq) != SZ(c[i])) {
          bad = 1;
          break;
        } else {
          for (int j = 0; j < SZ(c[i]); j++)
          if (seq[j] != c[i][j].first) {
            bad = 1;
            break;
          }
        }
      }
    }
    printf("Case #%d: ", tt );
    if (bad)
    printf("Fegla Won\n");
    else {
      int ans = OO;

      vector<pair<char, int> > ret;
      for(int i = 0; i < SZ(seq); i++)
      ret.push_back(MP(seq[i],1));

      for (int i = 0; i < n; i++) {
        int mn = 0;
        for (int j = 0; j < n; j++) {
          if (i == j)
          continue;
          for (int k = 0; k < SZ(c[j]); k++)
          mn += abs(c[j][k].second - c[i][k].second);
        }
        // cout<<i<<" "<<mn<<endl;
          ans = min(ans, mn);
        }

        int mn = 0;
        for (int j = 0; j < n; j++) {
          for (int k = 0; k < SZ(c[j]); k++)
          mn += abs(c[j][k].second - ret[k].second);
        }
        ans = min(ans, mn);

        printf("%d\n", ans);
      }

    }
    return 0;
  }
