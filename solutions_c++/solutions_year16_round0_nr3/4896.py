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

inline ll isDiv(ll x){
  for(ll i=2;i*i<=x;i++){
    if(x%i==0) return i;
  }
  return -1;
}

inline ll trans(ll bit, ll base, ll N){
  ll res = 0;
  rep(i,N){
    res *= base;
    if( (bit>>i)&1 ){
      res += 1;
    }
  }
  return res;
}

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    cout << "Case #" << casenum << ":" << endl;

    int N,J;
    cin >> N >> J;

    rep(bit,1<<(N-2)){
      ll num = 1;
      num = (num<<(N-2)) + bit;
      num = (num<<1) + 1;

      vector<ll> res;
      for(ll x=2;x<=10;x++){
	ll y = trans(num,x,N);
	ll d = isDiv(y);
	if(d<0)break;
	res.push_back(d);
      }

      if(res.size() == 9){
	cout << trans(num,10,N);
	rep(i,9){
	  cout << " " << res[i];
	}
	cout << endl;
	J--;
	if(J==0) break;
      }
    }
  }
}
