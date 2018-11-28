#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

#define dd(x)  cerr << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define SORT(c) sort((c).begin(),(c).end())
#define PB push_back

template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

using namespace std;

int main() {
  int problem_num;

  cin >> problem_num;
  FOR(pn,0,problem_num) {
    string s;
    cin >> s;

    string ans = "";
    ans += s[0];
    FOR(i,1,s.size()) {
      if (ans[0] <= s[i]) {
        ans = s[i] + ans;
      } else {
        ans = ans + s[i];
      }
    }
    printf("Case #%d: ", pn+1);
    cout << ans << "\n";
  }

  return 0;
}
