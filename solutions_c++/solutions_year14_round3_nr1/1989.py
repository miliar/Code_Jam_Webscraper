#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define D(x) cout << #x << " = " << x << endl;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define repd(i,a,b) for(int i=b-1;i>=a;i--)
#define REP(i,n) rep(i,0,n)
#define REPD(i,n) repd(i,0,n)
#define pb push_back
#define mp make_pair

typedef long long int lld;
typedef vector<int> vi;
typedef vector<lld> vlld;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const int INF = 1000;

int f(lld p, lld q, int cnt){
  if(p == 0) return cnt;
  if(cnt > 40 or p > q) return INF;

  if(q % 2) return INF;
  
  lld d = q / 2;
  int a = f(p - d, d, cnt+1);
  if(a <= 40) return cnt;

  int b = f(p, q/2, cnt+1);
  if(b <= 40) return b;

  return INF;
}

int main(){ IO;
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);

  int t;
  cin >> t;

  rep(ncase,1,t+1){
    cout << "Case #" << ncase << ": ";

    char tt;
    lld p, q;
    cin >> p >> tt >> q;

    int ans = f(p, q, 1);
    if(ans == INF) cout << "impossible" << endl;
    else cout << ans << endl;
  }

  return 0;
}
