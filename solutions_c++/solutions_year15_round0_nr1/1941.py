#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <iomanip>
#include <set>

#define INF 2000000000
#define MOD 1000000007

using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int testCount;
  cin >> testCount;
  for (int testNum = 1; testNum <= testCount; testNum++) {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int curSum = 0;
    int ans = 0;
    for (int i = 0; i <= n; i++) {
      if (curSum < i) {
	ans += i - curSum;
	curSum = i;
      }
      curSum += s[i] - '0';
    }
    cout << "Case #" << testNum << ": " << ans << endl;
  }
  return 0;
}
