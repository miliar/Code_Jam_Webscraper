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
typedef vector<ld> vld;
typedef set<ld> sld;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

void solveCase() {
  ll A, B, K;
  cin >> A >> B >> K;
  ll ret = 0;
  FOR(i, A) FOR(j, B) if ((i & j) < K) ret++;
  cout << ret << endl;
}

int main() 
{
  int t = GETINT;
  for (int test = 1; test <= t; test++) {
    cout << "Case #" << test << ": ";
    solveCase();
  }
  return 0;
}
