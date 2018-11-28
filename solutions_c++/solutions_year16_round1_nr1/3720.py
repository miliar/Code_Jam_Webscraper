#include <bits/stdc++.h>

using namespace std;

#define FOR(i,s,e) for(int (i)=(s);(i)<(int)(e);(i)++)
#define REP(i,e) FOR(i,0,e)
#define RFOR(i,e,s) for(int (i)=(e)-1;(i)>=(int)(s);(i)--)
#define RREP(i,e) RFOR(i,e,0)

#define all(o) (o).begin(), (o).end()
#define psb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))

typedef long long ll;
typedef pair<int, int> PII;
typedef queue<PII> QII;
typedef priority_queue<int, vector<int>, greater<int>> PQI;
typedef priority_queue<PII, vector<PII>, greater<PII>> PQII;

const double EPS = 1e-10;
int t;

int main() {
  scanf("%d ", &t);
  REP(cases, t) {
    string s, res;
    cin >> s;
    int n = (int)s.size();
    res += s[0];
    FOR(i,1,n) {
      if (res[0]<=s[i])
        res = s[i] + res;
      else
        res += s[i];
    }
    printf("Case #%d: ", cases+1);
    cout << res << endl;
  }

  return 0;
}

