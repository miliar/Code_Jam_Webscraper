#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

#define d(x)  cerr << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define SORT(c) sort((c).begin(),(c).end())
#define PB push_back

using namespace std;

int main() {
  int ans = 0;
  int problem_num;

  cin >> problem_num;

  FOR(pn,0,problem_num) {
    int n;
    cin >> n;
    string s;
    cin >> s;

    int count = 0;
    int ans = 0;

    FOR(i,0,n+1) {
      int current_num = s[i] - '0';
      if (current_num > 0) {
        if (i > count) {
          int add_count = i - count;
          ans += add_count;
          count += add_count;
        }
        count += current_num;
      }
    }

    printf("Case #%d: %d\n", pn+1, ans);
  }

  return 0;
}
