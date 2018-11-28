#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;

template <typename Type> void print_array(Type* array, int start, int end);
template <typename Type> void print_vector(vector<Type> v);

#define FOR(i,a,b) for (int i = (a),_b = (b); i < _b; i++)
#define DOW(i,b,a) for (int i = (b),_a = (a); i >= _a; i--)
#define fill(a,v) memset(a, v, sizeof a)
#define checkbit(n,b) ((n >> b) & 1)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()

#define INF 1e9
#define PI acos(-1.0)

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

int tc, cse = 1;
int n, k;
double p[300];
vector<double> probs;

double solve(int r, int h, int t){
	if(r == k && h == 0 && t == 0) return 1;
	else if (r == k || h < 0 || r < 0) return 0;
	else {
		return probs[r] * solve(r+1, h-1, t) + (1 - probs[r]) * solve(r+1, h, t-1);
	}
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  freopen("output.txt", "w", stdout);

  cin >> tc; 
  while(tc--){
  	cin >> n >> k;
  	FOR(i, 0, n) cin >> p[i];
  	double best = 0.0;
  	FOR(mask, 0, 1 << n){
  		if(__builtin_popcount(mask) != k) continue;
  		probs.clear();
  		FOR(i, 0, n){
  			if(checkbit(mask, i)) probs.push_back(p[i]);
  		}
  		best = max(best, solve(0, k/2, k/2));
  	}
  	cout << "Case #" << cse++ << ": "; 
  	cout << setprecision(10) << fixed << best << endl;
  }

  return 0;
}

template <typename Type>
void print_array(Type* array, int start, int end){
  cout << "[";
  FOR(i, start, end){
    cout << array[i] << " ";
  }
  cout << "]\n";
}

template <typename Type>
void print_vector(vector<Type> v){
  cout << "[";
  FOR(i, 0, SZ(v)){
    cout << v[i] << " ";
  }
  cout << "]\n";
}