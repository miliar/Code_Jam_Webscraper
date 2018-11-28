#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef long long ll;
typedef unsigned long long ull;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))

#define INF 0x3f3f3f3f
#define MAX 30

#define DEBUG false
#define debug(x) if (DEBUG) cout << #x << " = (" << x << ")\n"

priority_queue<ii> pq;
int v[MAX];

int main() {
  ios::sync_with_stdio(false);

  int T; cin >> T;

  FOR(t,1,T+1) {

      int n; cin >> n;
      int S = 0;
      FOR(i,0,n) {
          cin >> v[i];
          S += v[i];
          pq.push(ii(v[i], i));
      }

      cout << "Case #" << t << ":";
      while (!pq.empty()) {
          ii curr = pq.top(); pq.pop();
          ii next = pq.top(); pq.pop();
        //   cout << endl << (char)(curr.second + 'A') << ":" << curr.first << "\t" << (char)(next.second + 'A') << ":" << next.first << endl;
          if (curr.first*2 > (S-1) && next.first*2 > (S-1)) {
              // remove dois
              cout << " ";
              cout << (char)(curr.second + 'A') << (char)(next.second + 'A');
              curr.first--;
              if (curr.first) pq.push(curr);
              next.first--;
              if (next.first) pq.push(next);
              S -= 2;
          }
          else {
              if (curr.first*2 > (S-1)){
                  cout << " ";
                  cout << (char)(curr.second + 'A');
                  curr.first--;
                  if (curr.first) pq.push(curr);
                  pq.push(next);
                  S -= 1;
              }
              else {
                  cout << " ";
                  cout << (char)(curr.second + 'A');
                  curr.first--;
                  if (curr.first) pq.push(curr);
                  pq.push(next);
                  S -= 1;
              }
          }
      }
      cout << endl;

  }


  return 0;
}
