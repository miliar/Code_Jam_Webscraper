#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

int E, R, N;
vector<int> list;
map < PII , int > memo;

int find(int e, int n) {
  PII cur(e, n);
  if (memo.find(cur) != memo.end()) return memo[cur];
  if (n == N) return 0;

  memo[cur] = 0;
  int& ans = memo[cur];
  for (int i = 0; i <= e; i++) {
    ans = max(ans, i * list[n] + find(min(E, e - i + R), n + 1));
  }

  return ans;
}

void solveCase() {
  E = GETINT;
  R = GETINT;
  N = GETINT;
  list.clear();
  FOR(i, N) list.pb(GETINT);
  memo.clear();
  printf("%d\n", find(E, 0));
}

int main() 
{
  int t = GETINT;
  for (int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    solveCase();
  }
  return 0;
}
