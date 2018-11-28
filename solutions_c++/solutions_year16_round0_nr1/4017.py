#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <cassert>
#include <string.h>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define sz(x) int((x).size())
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

int solve(int x) {
  int result = 1;
  set<int> st;
  while (true) {
    ll tmp = x * result;
    do {
      st.insert(tmp%10);
      tmp /= 10;
    } while (tmp);
    if (st.size() == 10) break;
    ++result;
  }
  return result;
}


int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif
  int n; scanf("%d", &n);
  forn(i, n) {
    printf("Case #%d: ", i+1);
    int x; scanf("%d", &x);
    if (x == 0) printf("INSOMNIA\n");
    else cout << x * (ll) solve(x) << endl;
  }
	return 0;
}

