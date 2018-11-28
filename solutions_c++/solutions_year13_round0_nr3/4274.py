#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <cmath>

using namespace std;
typedef pair <int, int> P;
const long long MAXN = 100000000000000LL;

int t;
long long a, b;
bool pal(long long x);
vector <long long> r;

int main() {
  scanf("%d", &t);
  int num = 0;
  for(long long i = 1LL; i * i <= MAXN; ++i) {
      if(pal(i) && pal(i * i)) r.push_back(i * i);
  }
  while(t--) {
      ++num;
      scanf("%lld %lld", &a, &b);
      int res = 0;
      for(int i = 0; i < r.size(); ++i) {
	  if(r[i] >= a && r[i] <= b) ++res;
      }
      printf("Case #%d: %d\n", num, res);
  }
  return 0;
}

bool pal(long long x) {
    int nums[30];
    int act = 0;
    do {
	nums[act++] = x % 10;
	x /= 10;
    } while(x != 0);
    for(int i = 0; i < act; ++i) {
	if(nums[i] != nums[act - i - 1]) return false;
    }
    return true;
}