#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
typedef pair<LL, LL> PLL;

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define FF first
#define SS second
template<class S, class T>
istream& operator>>(istream& is, pair<S,T>& p){
  return is >> p.FF >> p.SS;
}

const double EPS = 1e-10;
const double PI  = acos(-1.0);
const LL MOD = 1e9+7;

int N, K;
int bc(int x){
  int res = 0;
  while(x > 0){
	res += x&1;
	x >>= 1;
  }
  return res;
}
double calc(vector<double>& q){
  double res = 0.;
  for(int b=(1<<(K/2))-1;b<(1<<K);++b){
	if(bc(b) != K/2) continue;
	double p = 1.;
	REP(i,K)
	  if(b>>i&1) p *= q[i];
	  else p *= (1.-q[i]);
	res += p;
  }
  return res;
}

double naive(int i, int k, vector<double>& ps, vector<double>& q){
  if(k == K){
	return calc(q);
  }
  if(i == N) return 0.;
  double res = naive(i+1,k,ps,q);
  q.PB(ps[i]);
  res = max(res, naive(i+1,k+1,ps,q));
  q.pop_back();
  return res;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(tt,1,T+1){
	cin >> N >> K;
	vector<double> ps(N);
	REP(i,N) cin >> ps[i];
	vector<double> tmp;
	double ans = naive(0,0,ps,tmp);
	cout << "Case #" << tt << ": " << fixed << setprecision(7) << ans  << endl;
  }
  
  return 0;
}
