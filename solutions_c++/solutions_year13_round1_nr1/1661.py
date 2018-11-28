#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long int ll;
typedef list<int> li;
typedef pair<int,int> pii;
typedef set<int> si;
typedef vector<int> vi;
typedef vector<vi> vii;

const double EPS = 1e-9;
const double PI = 3.14159265358979;

#define mp make_pair
#define Max(a,b) ( (a) > (b) ? (a) : (b) )
#define Min(a,b) ( (a) < (b) ? (a) : (b) )
#define Mod(x) ( (x) > 0 ? (x) : (-(x)) )

int main() {

  int TC, TCi;
  ll r,t;
  scanf("%d", &TC);
  
  for (TCi = 1; TCi <= TC; ++TCi) {
    printf("Case #%d: ", TCi);
    scanf("%lld%lld", &r, &t);

    ll ans = 0, sum = 0, k;
    ll fixo = 2 * r - 1;

    for (k = 1;  ; k += 2) {
      sum += 2 * k + fixo;

      if (sum <= t)
	++ans;
      else
	break;
    }
        
    printf("%lld\n", ans);
  }
  
  return 0;
}

  /*
    Input 
 	
    5
    1 9
    1 10
    3 40
    1 1000000000000000000
    10000000000000000 1000000000000000000


    Output 
 
    Case #1: 1
    Case #2: 2
    Case #3: 3
    Case #4: 707106780
    Case #5: 49
  */
