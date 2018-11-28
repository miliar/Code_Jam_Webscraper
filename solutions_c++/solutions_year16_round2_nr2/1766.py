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
typedef priority_queue<pair<int, PII>, vector<pair<int, PII>>, greater<pair<int, PII>>> PQIII;

const double EPS = 1e-10;
const int INF = 1e9;
int t;

int check(int x, int n, string cj) {
  REP(i,n) {
    if (cj[n-1-i] != '?' && (x % 10 != cj[n-1-i]-'0')) return 0;
    x /= 10;
  }
  return 1;
}

int main() {
  string c, jj;
  scanf("%d ", &t);
  REP(cases, t) {
    cin >> c >> jj;
    int n = (int)c.size();
    PQIII q;
    int m = 1;
    REP(i,n) m *= 10;
    REP(i,m) REP(j,m) if (check(i,n,c) && check(j,n,jj)) q.push(mp((int)abs(i-j), mp(i,j)));
    string resl, resr;
    REP(i,n) {
      resl += '0';
      resr += '0';
    }
    int resll = q.top().second.first, resrr = q.top().second.second;
    int i = 0;
    while (resll) {
      resl[n-1-i] = '0' + (resll % 10); 
      resll /= 10;
      i++;
    }
    i = 0;
    while (resrr) {
      resr[n-1-i] = '0' + (resrr % 10); 
      resrr /= 10;
      i++;
    }
    printf("Case #%d: ", cases+1);
    cout << resl << ' ' << resr << endl;
  }

  return 0;
}

