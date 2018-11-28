//Esteban Foronda Sierra
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <unordered_map>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r;}

#define ll long long
#define D(x) cout << #x << " " << x << endl
#define MAXN 1050
string x;

ll solve() {
  ll movements = 0;
  for(int i = 0; i < x.size() - 1; ++i) {
    if(x[i] != x[i + 1]) movements++;
  }
  if(x[x.size() - 1] == '-') movements++;
  return movements;
}


int main(){
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    cin >> x;
    printf("Case #%d: %lld\n", i + 1, solve());
  }
	return 0;
}
