#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>

using namespace std;
using namespace std::tr1;

typedef long long ll;
typedef pair<int, int> pii;
#define foreach(v,c) for (typeof((c).begin()) v = (c).begin(); v != (c).end(); ++v)
#define rep(i,s,e) for (int i = (s); i < (e); ++i)
#define X first
#define Y second
#define all(x) (x).begin(),(x).end()

int dx[]={0,0,1,-1,1,-1,1,-1};
int dy[]={-1,1,0,0,1,-1,-1,1};
const int mod = 1e9+7;

ll N;int M;
struct Traveller {
  int a, b, n;
};

Traveller t[2][1000100];
Traveller tmp[1000100];
int sz;
bool tt=0;

bool overlap(int i, int j) {
  if (t[tt][i].a < t[tt][j].a && t[tt][i].b >= t[tt][j].a && t[tt][i].b < t[tt][j].b) return 1;
  return 0;
}
int main() {
  ios_base::sync_with_stdio(false);
  int T;cin>>T;
  rep(tc,1,T+1) {
    tt=0;
    cin >> N >> M;
    rep(i,0,M)
      cin >> t[tt][i].a >> t[tt][i].b >> t[tt][i].n;
    sz=M;
    ll cost1 = 0;
    rep(i,0,M) {
      int d = t[tt][i].b-t[tt][i].a;
      cost1 += t[tt][i].n * ((N*(N+1) - (N-d)*(N-d+1))/2);
    }
    //cout << "c1=" << cost1 << endl;
    bool found;
    do {
      //cout << "iterating" << endl;
      found=0;
      memcpy(t[!tt],t[tt],sizeof t[tt]);
      int newsz=sz;
      rep(i,0,sz)
        rep(j,i+1,sz) {
          if (overlap(i,j) || overlap(j,i)) {
            //cout << "merging " << i << " " << j << endl;
            int m = min(t[tt][i].n, t[tt][j].n);
            t[tt][i].n -= m;
            t[tt][j].n -= m;
            t[!tt][i].n -= m;
            t[!tt][j].n -= m;
            t[!tt][newsz].a = min(t[tt][i].a, t[tt][j].a);
            t[!tt][newsz].b = max(t[tt][i].b, t[tt][j].b);
            t[!tt][newsz++].n = m;
            t[!tt][newsz].a = max(t[tt][i].a, t[tt][j].a);
            t[!tt][newsz].b = min(t[tt][i].b, t[tt][j].b);
            t[!tt][newsz++].n = m;
            found=1;
          }
        }
      tt = !tt;
      int i=0;
      //cout << "newsz=" << newsz << endl;
      rep(j,0,newsz) {
        if (t[tt][j].n) {
          if (i!=j) t[tt][i++]=t[tt][j];
          else i++;
        }
      }
      //cout << "i=" << i << endl;
      sz = i;
    } while (found);

    ll cost2 = 0;
    //cout << "sz=" << sz << endl;
    rep(i,0,sz) {
      //cout << "a=" << t[tt][i].a <<" b=" << t[tt][i].b << endl;
      int d = t[tt][i].b-t[tt][i].a;
      cost2 += t[tt][i].n * ((N*(N+1) - (N-d)*(N-d+1))/2);
    }
    //cout << "c2=" << cost2 << endl;
    cout << "Case #" << tc << ": " << (cost1-cost2) << endl;
  }
}
