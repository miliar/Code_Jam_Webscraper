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

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r;}

#define ll long long
#define D(x) cout << #x << " " << x << endl
#define pic pair <int, char>
vector <pic> parties;

vector <string> solve(int sum) {
  sort(parties.rbegin(), parties.rend());
  vector <string> ans;
  while(sum > 0) {
    int mini = min(parties[0].first, 2);
    int half = (sum - mini) / 2;
    if(parties[1].first <= half) {
      parties[0].first -= mini;
      string aux;
      for(int i = 0; i < mini; ++i) aux += parties[0].second;
      ans.push_back(aux);
      sum -= mini;
    } else {
      parties[0].first--;
      parties[1].first--;
      string aux;
      aux += parties[1].second;
      aux += parties[0].second;
      ans.push_back(aux);
      sum -= 2;
    }
    sort(parties.rbegin(), parties.rend());
  }
  return ans;
}

int main(){
  int t;
  cin >> t;
  for (int x = 1; x <= t; ++x) {
    int n;
    cin >> n;
    parties.clear();
    int sum = 0;
    for(int i = 0; i < n; ++i) {
      int members;
      cin >> members;
      sum += members;
      parties.push_back(pic(members, 'A' + i));
    }
    vector <string> ans = solve(sum);
    printf("Case #%d: %s", x, ans[0].c_str());
    for(int i = 1; i < ans.size(); ++i) printf(" %s", ans[i].c_str());
    printf("\n");
  }
  return 0;
}
