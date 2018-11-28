#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <fstream>
#include <thread>
#include <assert.h>
#include <sys/mman.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <iomanip>
#include <forward_list>

using namespace std;

bool check(vector<int>& v, int sum) {
  for (int x : v) {
    if (x*2 > sum) {
      return false;
    }
  }
  return true;
}

void dopr(int c1, int c2) {
  string s = " ";
  s += 'A' + c1;
  if (c2 != -1)
    s += 'A' + c2;
  cout << s;
}

void solve(int casenum) {
  printf("Case #%d:", casenum);
  int n;
  cin >> n;

  vector<int> v;
  v.reserve(n);

  int sum = 0;
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    v.push_back(x);
    sum += x;
  }

  while (sum > 0) {
    int max1 = -1;
    int max2 = -1;
    for (int i = 0; i < v.size(); ++i) {
      if (v[max1] < v[i]) {
        max2 = max1;
        max1 = i;
      } else if (v[max2] < v[i]) {
        max2 = i;
      }
    }
    if (sum == 1) {
      dopr(max1, -1);
      continue;
    }
    if (v[max1] > 1) {
      v[max1]-= 2;
      if (check(v, sum-2)) {
        dopr(max1, max1);
        sum -= 2;
        continue;
      }
      v[max1] += 2;
    }
    v[max1]--;
    v[max2]--;
    if (check(v, sum - 2)) {
      sum -= 2;
      dopr(max1, max2);
      continue;
    }
    v[max2]++;
    if (check(v, sum - 1)) {
      sum -= 1;
      dopr(max1, -1);
      continue;
    }
    assert(false);
  }
  cout << "\n";
}

int main(int argc, const char * argv[]) {
  freopen("file.txt","r",stdin);
  freopen("file.out","w",stdout);

  int t = 0;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; ++i) {
    solve(i);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
