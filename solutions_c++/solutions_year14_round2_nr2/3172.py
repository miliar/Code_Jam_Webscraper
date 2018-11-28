#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <list>
using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
// 初期化！
int t, a, b, k;

int solve() {
  vector<int> bitwise_and;
  int ba;
  rep(i,a) {
    rep(j,b) {
      ba = i & j;
      // printf("i = %d, j = %d,  i & j = %d\n", i, j, ba);
      bitwise_and.push_back(ba);
      // vector<int>::iterator pos;
      // pos = find(bitwise_and.begin(), bitwise_and.end(), ba);
      // if (pos == bitwise_and.end()) { // new number
      // 	bitwise_and.push_back(ba);
      // 	}
    }
  }
  sort(bitwise_and.begin(), bitwise_and.end());
  int ret = 0;
  int len = bitwise_and.size();
  rep(i,k) {
    rep(j,len) {
      if (bitwise_and.at(j) == i) {
	ret++;
      }
    }
  }
  return ret;


}

int main() {
  cin >> t;
  rep(i,t) {
    cin >> a >> b >> k;
    int ans = solve();
    printf("Case #%d: %d\n", i+1, ans);
  }
  return 0;
}
