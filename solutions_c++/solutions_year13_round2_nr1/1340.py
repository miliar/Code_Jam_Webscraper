#include <iostream>
//#include <cstdio>
//#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
//#include <map>
//#include <set>
//#include <queue>
//#include <limits>
//#include <sstream>
//#include <functional>
using namespace std;

#define len(array)  (sizeof (array) / sizeof *(array))
#define rep(i, s, e) for(int i = s;i < e;i++)
#define rrep(i, e, s) for(int i = e;s <= i;i--)
#define mfill(a, v) fill(a, a + len(a), v)
#define mfill2(a, v, t) fill((t *)a, (t *)(a + len(a)), v)
#define vsort(v) sort(v.begin(), v.end())
#define rvsort(v, t) sort(v.begin(), v.end(), greater<t>())
#define asort(a) sort(a, a + len(a))
#define rasort(a, t) sort(a, a + len(a), greater<t>())
#define dmax(a, b) (a < b? b : a)
#define dmin(a, b) (a > b? b : a)
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> P;
const int INF = (int)1e9;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-10;
//const int dx[] = {1, -1, 0, 0, 1, -1, -1, 1};
//const int dy[] = {0, 0, 1, -1, -1, -1, 1, 1};
//const int weight[] = {0,1,10,100,1000,10000,100000,1000000,10000000};
typedef struct _Node {
  _Node(int arg1 = 0, int arg2 = 0 , int arg3 = 0) {
	i = arg1;
	j = arg2;
	k = arg3;
  }
  int i,j,k;
  bool operator <(const struct _Node &e) const{
    return i == e.i? j < e.j : i < e.i;
  }
  bool operator >(const struct _Node &e) const{
    return i == e.i? j > e.j : i > e.i;
  }
}node;

int n;
ll others[1000002];

int step(int p, ll mote){
  //cout << p << ", " << mote << endl;
  int tr = 0;
  ll tmp = mote, res;
  if(p == n) return 0;
  if(mote == 1) return n - p;
  while(mote <= others[p]){
	mote += mote - 1;
	tr++;
  }
  mote += others[p];
  res = tr + step(p+1, mote);
  return dmin(n - p, res);
}

void doIt(){
  ll t, a;
  cin >> t;
  rep(ii, 0, t){
	int op = 0;
	cin >> a >> n;
	rep(i, 0, n){
	  cin >> others[i];
	}
	sort(others, others + n);
	cout << "Case #" << (ii+1) << ": " << step(0, a) << endl;
  }
}

int main() {
  doIt();
  return 0;
}
