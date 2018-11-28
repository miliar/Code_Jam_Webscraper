#include <bits/stdc++.h>
using namespace std;
#define all(c) (c).begin(),(c).end()
#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define iter(c) __typeof((c).begin())
#define tr(it,c) for(iter(c) it=(c).begin(); it!=(c).end(); it++)
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define pr(a) cout << (a) << endl
typedef long long ll;
typedef pair<int,int> P;
const int MAX=1000000000;
int dx[4]={-1,0,1,0},dy[4]={0,-1,0,1};

double c,f,x,ans;
void solve(double a, double t) {
  if(ans>x/a+t) ans=x/a+t;
  else return;
  double d=c/a;
  solve(a+f,t+d);
}

int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++) {
    cin >> c >> f >> x;
    ans=1000000000.0;
    solve(2.0,0.0);
    cout << "Case #" << t << ": ";
    printf("%.7f\n",ans);
  }
  return 0;
}
