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

int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++) {
    int a[17];
    fill(a,a+17,0);
    int n;
    for(int k=0; k<2; k++) {
      cin >> n;
      for(int i=0; i<4; i++) {
	for(int j=0; j<4; j++) {
	  int x;
	  cin >> x;
	  if(i+1==n) a[x]++;
	}
      }
    }
    int cnt=0,ans;
    for(int i=1; i<17; i++) {
      if(a[i]==2) {
	cnt++;
	ans=i;
      }
    }
    cout << "Case #" << t << ": ";
    if(cnt==0) cout << "Volunteer cheated!" << endl;
    else if(cnt>1) cout << "Bad magician!" << endl;
    else cout << ans << endl;
  }
  return 0;
}
