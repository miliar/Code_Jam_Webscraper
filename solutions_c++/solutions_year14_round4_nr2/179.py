#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;
 int N;
 long long arr[1000];
void doit (int casenum) {
  cin >> N;
  for(int i = 0; i < N; ++i)
    cin >> arr[i];
  int b = 0;
  int e = N;
  long long cnt = 0;
  for(int z = 0; z < N; ++z) {
    long long m = 1000000000000ll;
    int p = -1;
    for(int i = b; i < e; ++i) {
      if(arr[i] < m) {
        m = arr[i];
        p = i;
      }
    }
    if(p < 0)
      std::abort();
    int left = p - b;
    int right = e - p - 1;
    if(left < right) {
      while(p > b) {
        ++cnt;
        std::swap(arr[p-1], arr[p]);
        --p;
      }
      ++b;
    } else {
      while(p + 1 < e) {
        ++cnt;
        std::swap(arr[p], arr[p+1]);
        ++p;
      }
      --e;
    }
  }
  std::cout << "Case #" << casenum << ": " << cnt << "\n";
}

int main () {
  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i)
    doit(i);
  return 0;
}