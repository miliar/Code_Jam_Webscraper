

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

void mark_used(LL x, vector<bool>& used) {
  while (x > 0) {
    int dig = x % 10;
    used[dig] = true;
    x /= 10;
  }
}

bool all_true(const vector<bool>& v) {
  for (int i=0; i<v.size(); i++) {
    if (!v[i]) return false;
  }
  return true;
}

pair<int,LL> multiple(int x) {
  vector<bool> used(10, false);
  LL tmp = 0;
  int ans = 0;
  while (!all_true(used)) {
    tmp += x;
    ans++;
    mark_used(tmp, used);
  }
  return make_pair(ans, tmp);
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  cin.tie(NULL);
  int T, N;
  cin >> T;
  for (int i=0; i<T; i++) {
    cin >> N;
    cout << "Case #" << i+1 << ": ";
    if (N==0) cout << "INSOMNIA" << endl;
    else {
      auto ans = multiple(N);
      cout << ans.second << endl;
    }
  }
}
