#include <iostream>
#include <complex>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
#include <set>
#include <limits>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define REP(i, j) for(int i = 0; i < (int)(j); ++i)
#define FOR(i, j, k) for(int i = (int)(j); i < (int)(k); ++i)
#define P pair<int, int>
#define SORT(v) sort((v).begin(), (v).end())
#define REVERSE(v) reverse((v).begin(), (v).end())
const int N = 4;

int main() {
  int T; cin >>T;
  int v[N][N];
  REP(t, T){
    int fir; cin >>fir;
    set<int> s;
    vector<int> ans;
    REP(i, N)
      REP(j, N){
        cin >>v[i][j];
        if(i + 1 == fir) s.insert(v[i][j]);
      }
    int sec; cin >>sec;
    REP(i, N)
      REP(j, N){
        cin >>v[i][j];
        if(i + 1 == sec && s.find(v[i][j]) != s.end()) ans.push_back(v[i][j]);
      }
    int cnt = (int)(ans.size());
    cout <<"Case #" <<t + 1 <<": ";
    if(cnt == 0) cout <<"Volunteer cheated!" <<endl;
    else if(cnt > 1) cout <<"Bad magician!" <<endl;
    else cout <<ans[0] <<endl;
  }
  return 0;
}
