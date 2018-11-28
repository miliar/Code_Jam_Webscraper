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

void solveCase() {
  int N, M;
  N = GETINT; M = GETINT;
  int arr[100][100], init[100][100];
  FOR(i, N) FOR(j, M) {
    arr[i][j] = GETINT;
    init[i][j] = 100;
  }

  FOR(i, N) {
    int mx = 0;
    FOR(j, M) mx = max(arr[i][j], mx);
    FOR(j, M) init[i][j] = mx;
  }

  FOR(j, M) {
    int mx = 0;
    FOR(i, N) mx = max(arr[i][j], mx);
    FOR(i, N) init[i][j] = min(init[i][j], mx);
  }

  FOR(i, N) FOR(j, M) if(init[i][j] != arr[i][j]) {
    printf("NO\n");
    return;
  }

  printf("YES\n");
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
