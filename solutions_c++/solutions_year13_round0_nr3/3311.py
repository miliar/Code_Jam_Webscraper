#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

bool is_palin(ll x) {
  vi num;
  while (x) {
    num.pb(x%10);
    x /= 10;
  }

  int i;
  fr (i, SZ(num)) if (num[i] != num[SZ(num) - i - 1]) return false;
  return true;
}

vector<ll> list;
void proc(string& s, int idx) {
  if (idx > SZ(s) - idx - 1) {
    int i;
    ll x = 0;
    fr (i, SZ(s)) x = x*10 + (s[i] - '0');
    if (is_palin(x*x)) {
      list.pb(x*x);
    }
    return;
  }

  int i;
  for(i = (idx == 0 ? 1 : 0); i <= 9; ++i) {
    s[idx] = s[SZ(s) - idx - 1] = (char)('0' + i);
    proc(s, idx + 1);
  }
}

int main() {
  int i, tc, cn = 0;
  for (int len = 1; len <= 7; ++len) {
    string s;
    fr (i, len) s.pb((char)(i + '0'));
    proc(s, 0);
  }

  cin >> tc;
  ll A, B;
  while (cn++ < tc) {
    cin >> A >> B;
    int cnt = 0;
    fr (i, SZ(list)) if (A <= list[i] && list[i] <= B) cnt++;
    cout << "Case #" << cn << ": " << cnt << endl;
  }
  return 0;
}
