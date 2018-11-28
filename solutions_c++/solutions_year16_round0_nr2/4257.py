#include <bits/stdc++.h>

#define F first
#define S second
#define llong long long
#define ullong unsigned long long
#define mp make_pair
#define pb push_back
#define pii pair <int, int>
#define sz(v) (int)v.size()

using namespace std;

const int MXN = (int)1e6 + 10;
const int INF = (int)1e9 + 7;
const llong LINF = (llong)1e18 + 10;
const double EPS = (double)1e-9;
const double PI = (double)acos(-1.0);

int n;
string s;
int T;

int main(){
  #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif // LOCAL
  cin >> T;
  for(int tests = 1; tests <= T; ++tests){
    cin >> s;
    n = sz(s) - 1;
    while(n >= 0 && s[n] == '+')
      --n;
    ++n;
    int ans = 0;
    for(int i = 1; i < n; ++i){
      if(s[i] != s[i - 1])
        ++ans;
    }
    if(n)
      ++ans;
    cout << "Case #" << tests << ": " << ans << "\n";
  }
  return 0;
}
