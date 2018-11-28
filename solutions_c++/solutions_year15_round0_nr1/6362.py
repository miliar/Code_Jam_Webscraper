//mishraiiit
#include<bits/stdc++.h>
#define ll long long int
using namespace std;
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
#define foreach(v, c) for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
typedef pair <ll, ll> pll;

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

int main() {

    fastScan;

    ll t, n;
    string s;
    cin >> t;

    ll num = 0;

    while(t--) {
      num++;
      cin >> n >> s;
      ll sum = 0, ans = 0;
      for(int i = 0; i < s.size(); i++) {
        if(sum < i)
          ans = ans + (i - sum), sum = i;
        sum = sum + (s[i] - '0');
      }
      cout << "Case #" << num << ": " << ans << endl;
    }

    return 0;
}
