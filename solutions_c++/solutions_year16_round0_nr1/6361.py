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

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  freopen("test.in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
  int fin = (1 << 10) - 1, t, n;
  cin >> t;
  FOR (cs , 1, t + 1)
  {
    cin >> n;
    int c = 0, x = 0;
    while (c != fin) {
      x += n;
      int cc = x;
      while (cc)
        c |= (1 << (cc % 10)), cc /= 10;
      if (n == 0) {
        x = -1;
        break;
      }
    }
    if (x == -1)
      cout << "Case #" << cs << ": " << "INSOMNIA" << endl;
    else
      cout << "Case #" << cs << ": " << x << endl;
  }
  return 0;
}
