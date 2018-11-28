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

void solve(string x, int i) {
  string ans = " ";
  ans[0] = x[0];
  for(int i = 1; i < x.size(); ++i) {
    if(x[i] >= ans[0]) ans = x[i] + ans;
    else ans += x[i];
  }
  printf("Case #%d: %s\n", i, ans.c_str());
}


int main(){
  int n;
  cin >> n;
  for(int i = 1; i <= n; ++i) {
    string s;
    cin >> s;
    solve(s, i);
  }
	return 0;
}
