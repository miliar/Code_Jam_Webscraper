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

int tc, cse = 1, cmask, curr, mac[5], n;
vi success[10], order;
bool over = false;

void dfs(int k){
	int n = SZ(order);
	if(k == n) return;
	int part = cmask / (1 << order[k] * n);
	part %= (1 << n);
	FOR(i, 0, n) if(mac[i]) part ^= (1 << i);
	if(part == 0) over = true;
	else {
		FOR(j, 0, n){
			if(checkbit(part, j)){
				mac[j] = 1;
				dfs(k+1);
				mac[j] = 0;
			}
		}
	}
}

bool fail(int mask){
	fill(mac, 0);
	cmask = mask;
	over = false;
	dfs(0);
	return over;
}

bool can(int n, int mask){
	order.clear();
	FOR(i, 0, n) order.push_back(i);
	do {
		if(fail(mask)) return false;
	} while(next_permutation(ALL(order)));
	return true;
}

int main() {
  freopen("output.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  success[1].push_back(1);
  FOR(mask, 0, 1 << 4){
	if(can(2, mask)) success[2].push_back(mask);  	
  }

  FOR(mask, 0, 1 << 9){
	if(can(3, mask)) success[3].push_back(mask);  	
  }

  FOR(mask, 0, 1 << 16){
	if(can(4, mask)) success[4].push_back(mask);  	
  }
  //FOR(i, 1, 5) print_vector(success[i]);
  cin >> tc; 
  while(tc--){
  	cin >> n;
  	int val = 0;
  	string nxt;
  	FOR(i, 0, n){
  		cin >> nxt;
  		FOR(j, 0, n){
  			val *= 2;
  			if(nxt[j] == '1') val++;
  		}
  	}
  	int best = 100;
  	//cout << val << endl;
  	FOR(i, 0, SZ(success[n])){
  		if((success[n][i] | val) != success[n][i] || (success[n][i] & val) != val) continue;  
  		//if(__builtin_popcount(success[n][i] - val) < best) cout << success[n][i] << endl;
  		best = min(best, __builtin_popcount(success[n][i] - val));
  	}
  	cout << "Case #" << cse++ << ": "; 
  	cout << best << endl;
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