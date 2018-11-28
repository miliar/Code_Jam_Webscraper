#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <climits>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define SORT(c) sort((c).begin(),(c).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
const double EPS = 1e-10;
const double PI  = acos(-1.0);

LL gcd(LL x, LL y){
  if(y == 0) return x;
  return gcd(y, x%y);
}

LL lcm(LL x, LL y){
  return x*y/gcd(x,y);
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(t,1,T+1){
	int B, N; cin >> B >> N;
	VI ms(B);
	REP(i,B) cin >> ms[i];
	
	vector<int> ok(B, 0);
	LL c = B;
	REP(i,B) ok[i] = ms[i];
	for(;;){
	  bool fl = true, up = false;
	  for(int i=0;i<B;++i){
		if(ok[i] != 0){
		  fl = false;
		}
		else{
		  ok[i] = ms[i];
		  ++c;
		  up = true;
		}
	  }
	  if(fl) break;
	  if(!up){
		for(int i=0;i<B;++i)
		  --ok[i];
	  }
	}
	c -= B;
	
	--N;
	N = N % c;
	int ans = -1;
	fill(ALL(ok), 0);
	for(int i=0;N>=0;++i){
	  int idx = -1;
	  for(int j=0;j<B;++j){
		if(ok[j] == 0){
		  idx = j;
		  ok[j] += ms[j];
		  break;
		}
	  }
	  if(idx < 0)
		REP(j,B) ok[j]--;
	  else{
		ans = idx;
		--N;
	  }
	}
	
	cout << "Case #" << t << ": " << ans+1 << endl;
  }
  
  return 0;
}
