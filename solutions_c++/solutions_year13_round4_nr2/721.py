#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
typedef  long long   ll;


#define ALL(x)   (x).begin(),(x).end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);




template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}


long long N, P;


long long getWorst(long long quedan, int ind) {
//  cout << quedan << "  " << ind << endl;
  if (ind == N) return 0;
  quedan = min(quedan, (1LL<<(N-ind))-1LL);
//  cout << "  AFTER  " <<  quedan << "  " << ind << endl;
  long long res = 0;
  if (quedan) {
    res = getWorst((quedan-1LL)/2LL, ind+1) | (1LL << (N-1-ind));
  } else {
    res = getWorst((quedan-1LL)/2LL, ind+1);
  }
  return res;
}

long long getBest(long long quedan, int ind) {
  if (ind == N) return 0;
 // cout << quedan << "  " << ind << endl;
  quedan = min(quedan, (1LL<< (N-ind)) - 1LL);
//  cout << "  AFTER  " <<  quedan << "  " << ind << endl;
  long long res = 0;
  if (quedan) {
    res = getBest((quedan-1LL)/2LL, ind+1);
  } else {
    res = getBest((quedan-1LL)/2LL, ind+1) | (1LL << (N-1-ind));
  }
  return res;
}


int main() {
  int i,j ,k;
  int casos; cin >> casos; for (int h = 0 ; h < casos ; ++h ) {
    cin >> N >>  P;
    // busquemos el ultimo que si o si saca premio... 
    long long b = 0, e = 1LL << N;
    while (b + 1LL < e) {
      if (getWorst((b+e)/2LL, 0) < P)
        b = (b+e)/2LL;
      else e = (b+e)/2LL;
    }
    long long always = b;
    // El que podria llegar  a sacar puesto... 


    b = 0, e = 1LL << N;
    long long TOT = 1LL << N;
    while (b + 1LL < e) {
      if (getBest(TOT-1LL-(b+e)/2LL, 0) < P)
        b = (b+e)/2LL;
      else e = (b+e)/2LL;
    }
    long long sometimes = b;

    cout << "Case #" << h+1 << ": " << always << " " << sometimes << endl;
  }return 0;
  
}
