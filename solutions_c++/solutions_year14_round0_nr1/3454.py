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
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);

  int t;
  cin >> t;

  rep(ncase,1,t+1){
    cout << "Case #" << ncase << ": ";

    int r1, r2;
    int board1[4][4], board2[4][4];

    cin >> r1; r1--;
    REP(i,4) REP(j,4) cin >> board1[i][j];

    cin >> r2; r2--;
    REP(i,4) REP(j,4) cin >> board2[i][j];


    vi cnt(17,0);
    REP(j,4) cnt[board1[r1][j]]++;
    REP(j,4) cnt[board2[r2][j]]++;

    vi ans;
    rep(i,1,17) if(cnt[i] == 2) ans.pb(i);
    
    if(ans.size() == 0) cout << "Volunteer cheated!" << endl;
    if(ans.size() == 1) cout << ans[0] << endl;
    if(ans.size() >= 2) cout << "Bad magician!" << endl;
  }

  return 0;
}
