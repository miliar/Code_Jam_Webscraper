#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(a) (a).begin(),(a).end()
#define INIT(a) memset((a),0,sizeof(a))
#define fs first
#define sc second
#define pb push_back
#define sz size() 
using namespace std;
typedef long long ll;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;

const static int INF = 1e8;
const static D EPS = 1e-8;

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    int n;
    cin >> n;
    vi a(n);
    rep(i,n)cin >> a[i];

    int ans = 0;
    while(n){
      int argmin = 0;
      rep(i,n){
	if(a[i] < a[argmin])argmin = i;
      }

      ans += min(argmin,n-1-argmin);
      a.erase(a.begin()+argmin);
      n--;
    }

    cout << "Case #" << casenum << ": " << ans << endl;;
  }
}
