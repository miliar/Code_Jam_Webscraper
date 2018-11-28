#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
int solve(vector<int> v) {
  int ret = 0;
  while (true) {
    sort(ALL(v));
    reverse(ALL(v));
    if (v[0] == 0) {
      break;
    }
    if (v[0] % 2 == 0 && v[0] > 2) {
      v[0] /= 2;
      v.push_back(v[0]);
    }
    else {
      REP(i, SIZE(v)) {
        v[i]--;
      }
    }
    ret++;
  }
  return ret;
}

int solve2(vector<int> v, int steps) {
  sort(ALL(v));
  reverse(ALL(v));
  vector<int> t;
  vector<int> t2;
  REP(i, SIZE(v)) {
    t.push_back(v[i]);
    t2.push_back(v[i]);
  }
  if (t[0] == 0) {
    return 0;
  }
  for (int i = 0; i < SIZE(t); i ++) {
    t[i]--;
  }
  int ret = 1 + solve2(t, steps + 1);
  if (v[0] > 1) {
    int carry = t2[0] / 2;
    int start = max(1, carry - 1);
    if (t2[0] % 2 == 0) {
      start = carry;
    }
    for (int c = start; c <= carry; c ++) {
      t2.push_back(c);
      t2[0] -= c;
      ret = min(ret, 1 + solve2(t2, steps + 1));
      t2[0] += c;
      t2.pop_back();
    }
  }

  return ret;
}
int main() {
	//freopen("b.in", "r", stdin); 
//  freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt1.txt", "w", stdout);
	freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.txt", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	//freopen("B-small-attempt3.in", "r", stdin); freopen("B-small-attempt3.out", "w", stdout);
	
	//freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	
	int nT;
	cin>>nT;
	for (int t=1; t<=nT; t++) {
    vector<int> v;
    int N; 
    cin>>N;
    REP(i, N){
      int k; cin>>k;
      v.push_back(k);
    }
    
		printf("Case #%d: %d\n", t, solve2(v, 0));
	}
	return 0;
}
