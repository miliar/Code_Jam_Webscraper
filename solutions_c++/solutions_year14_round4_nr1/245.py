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
    int n,x;
    cin >> n >> x;
    vi a(n);
    rep(i,n)cin >> a[i];
    sort(all(a));

    int cnt = 0;
    rep(i,a.sz){
      int pos = upper_bound(all(a),x-a[i]) - a.begin()-1;
      if(i<pos && a[pos]<=x-a[i])a.erase(a.begin()+pos);
      a.erase(a.begin()+i); i--;
      cnt++;
    }

    cout << "Case #" << casenum << ": " << cnt << endl;;
  }
}
