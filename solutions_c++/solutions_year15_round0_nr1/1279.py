

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
    a << "{";
    if (v.size()>0) a << v[0];
    for (int i=1; i<v.size(); i++) a << ", " << v[i];
    a << "}";
    return a;
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC,N;
    string str;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> N >> str;
      int total = 0;
      int ans = 0;
      for (int i=0; i<=N; i++) {
        if (i > total) {
          int x = i - total;
          ans += x; total += x;
        }
        total += str[i]-'0';
      }
      cout << "Case #" << tc << ": " << ans << endl;
    }
}
