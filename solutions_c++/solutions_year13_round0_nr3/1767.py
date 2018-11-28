#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;

const int FIAR_AMOUNT = 39;
const LL FAIR[FIAR_AMOUNT] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};

int test_cases, result;
LL A, B;


bool is_palindrom(LL x) {
  LL i = x, j = 0;

  while(x>0) {
    j=(10*j) + (x%10);
    x/=10;
  }

  return i==j;
}

bool is_fair(int x) {
  float sq = sqrt(x);
  if(sq != floor(sq)) return false;

  return is_palindrom((int)sq);
}

bool is_OK(int x) {
  return (is_palindrom(x) && is_fair(x));
}


int main() {

  scanf("%d", &test_cases);
  FOR(test_case, 1, test_cases) {

    scanf("%lld%lld", &A, &B);
    result = 0;

/*
    a = ceil(sqrt(A)); b = floor(sqrt(B));
    FOR(n,a,b) {
      if(is_palindrom(n) && is_palindrom((LL)n*n)) printf("%lld ", (LL)n*n);
    } 
*/

    REP(i, FIAR_AMOUNT) {
      result += ((A<=FAIR[i]) && (FAIR[i]<=B));
    }

    printf("Case #%d: %d\n", test_case, result);
  }

  return 0;
}