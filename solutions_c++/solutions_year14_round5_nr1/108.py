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
typedef long double D;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ll> vl;

const static int INF = 1e8;
const static D EPS = 1e-8;

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    int n,p,q,r,s;
    cin >> n >> p >> q >> r >> s;
    vl t(n+1,0);
    for(ll i=0;i<n;i++)t[i+1] = t[i] + (i*p+q) % r + s;

    ll ans = 0;
    rep(i,n){
      if(n-i==1){
	ans = max(ans, min(t[i],t[n]-t[i]) );
      }else{
	ll l = i-1, r = n;
	ll search = (t[n] - t[i] + 1) / 2;
	while(r>l+1){
	  ll mid = (l+r)/2;
	  if(t[mid]-t[i] < search)l = mid;
	  else r = mid;
	}
	
	ll maxv = max(t[i],
		      min(max(t[n]-t[r],t[r]-t[i]),
			  max(t[n]-t[r-1],t[r-1]-t[i])));
	ans = max(ans, t[n] - maxv);
      }
    }

    cout << "Case #" << casenum << ": ";
    cout << fixed << setprecision(10) << (D)ans/t[n] << endl;
  }
}
