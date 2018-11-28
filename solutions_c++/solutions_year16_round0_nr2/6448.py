#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define mt make_tuple // ignore#define eb emplace_back#define endl '\n'
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

void flip(string &s, int idx) {
  reverse(s.begin(), s.begin() + idx + 1);
  FOR (i , 0 , idx + 1)
    s[i] = (s[i] == '+' ? '-' : '+');
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  freopen("test.in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
  int t;
  cin >> t;
  FOR (cs , 1, t + 1)
  {
    string s;
    cin >> s;
    int lst = sz(s) - 1, res = 0;
    while (7) {
      if (count(all(s), '+') == sz(s))
        break;
      lst = sz(s) - 1;
      while (lst >= 0 && s[lst] == '+')
        lst --;
      if (s[0] == '-') {
        flip(s, lst);
      }
      else {
        int pos = 0;
        while (pos < sz(s) && s[pos] == '+')
          pos ++;
        pos --;
        flip(s, pos);
      }
      res ++;
    }
    cout << "Case #" << cs << ": " << res << endl;
  }
  return 0;
}
