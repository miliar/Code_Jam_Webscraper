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
string ans[15][5];

int main() {
	freopen("output.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  ans[0][0] = 'R';
  ans[0][1] = 'P';
  ans[0][2] = 'S';

  FOR(i, 1, 14){
  	ans[i][0] = min(ans[i-1][0] + ans[i-1][2], ans[i-1][2] + ans[i-1][0]);
  	ans[i][1] = min(ans[i-1][1] + ans[i-1][0], ans[i-1][0] + ans[i-1][1]);
  	ans[i][2] = min(ans[i-1][1] + ans[i-1][2], ans[i-1][2] + ans[i-1][1]);
  }

  // FOR(i, 0, 3) FOR(j, 0, 5){
  // 	cout << ans[j][i] << endl;
  // }

  cin >> tc; 
  while(tc--){
  	int n, r, p, s;
  	cin >> n >> r >> p >> s;
  	string sol = "ZZZ";
  	FOR(i, 0, 3){
  		int rc = 0, pc = 0, sc = 0;
  		for(char c : ans[n][i]){
  			if(c == 'R') rc++;
  			else if (c == 'P') pc++;
  			else sc++;
  		}
  		//cout << rc << pc << sc << endl;
  		if(rc == r && pc == p && sc == s){
  			sol = min(sol, ans[n][i]);
  		}
  	}
  	cout << "Case #" << cse++ << ": "; 
  	if(sol == "ZZZ") cout << "IMPOSSIBLE" << endl;
  	else cout << sol << endl;
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