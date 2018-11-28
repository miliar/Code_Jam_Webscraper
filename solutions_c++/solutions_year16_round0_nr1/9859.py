#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <algorithm>

using namespace std;

#define rep(i,j) REP((i), 0, (j))
#define REP(i,j,k) for(int i=(j);(i)<(k);++i)
#define BW(a,x,b) ((a)<=(x)&&(x)<=(b))
#define ALL(v) (v).begin(), (v).end()
#define LENGTHOF(x) (sizeof(x) / sizeof(*(x)))
#define AFILL(a, b) fill((int*)a, (int*)(a + LENGTHOF(a)), b)
#define SQ(x) ((x)*(x))
#define Mod(x, mod) (((x)+(mod)%(mod))
#define MP make_pair
#define PB push_back
#define Fi first
#define Se second
#define INF (1<<29)
#define EPS 1e-10
#define MOD 1000000007

typedef pair<int, int> pi;
typedef pair<int, pi> pii;
typedef vector<int> vi;
typedef queue<int> qi;
typedef long long ll;

int main()
{

  int T;
  cin >> T;
  rep(t,T){
    set<int>S;

    ll N;
    cin >> N;
    if(N == 0){
      cout << "Case #" << t+1 << ": INSOMNIA" << endl;
      continue;
    }
    int c = 0;
    while(S.size() < 10){
      c++;      
      ll x = N*c;
      while(x){
	S.insert(x%10);
	x /= 10;
      }
    }

    cout << "Case #" << t+1 << ": " << c*N << endl;
  }
  return 0;
}
