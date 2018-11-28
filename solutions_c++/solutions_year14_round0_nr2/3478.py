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

int main(){ IO;
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);

  int t;
  cin >> t;

  rep(ncase,1,t+1){
    cout << "Case #" << ncase << ": ";

    double c, f, x;
    cin >> c >> f >> x;

    double ans = 0;
    double r = 2.0;
    while(true){
      double t0 = (c / r) + (x / (r + f));
      double t1 = x / r;

      if(t0 < t1){
        ans += c / r;
        r += f;
      }else{
        ans += t1;
        break;
      }
    }
    cout << std::setprecision(7) << fixed << ans << endl;
  }
  
  return 0;
}
