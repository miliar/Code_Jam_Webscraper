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
    string s;
    cin >> s;

    int count = 0;
    char flip = s[0];
    FOR(i,1,s.size()) {
      if (s[i] != flip) {
        flip = s[i];
        count++;
      }
    }
    if (s[s.size()-1] == '-') count++;
    printf("Case #%d: %d\n", pn+1, count);
  }

  return 0;
}
