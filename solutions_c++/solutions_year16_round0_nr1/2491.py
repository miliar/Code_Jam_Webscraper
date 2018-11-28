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


VS m;
VS m_out;
using namespace std;

int main() {
  int problem_num;

  cin >> problem_num;
  FOR(pn,0,problem_num) {
    LL n;
    cin >> n;

    if (n==0) {
      printf("Case #%d: INSOMNIA\n", pn+1);
      continue;
    }

    set<int> st;

    for(LL j=1;;++j) {
      LL num = j*n;
      string s = toString(num);
      FOR(i,0,s.size()) {
        // printf("hoge %d\n", s[i]);
        st.insert(s[i]);
      }
      if (st.size()==10) {
        printf("Case #%d: %lld\n", pn+1, num);
        break;
      }
    }
  }

  return 0;
}
