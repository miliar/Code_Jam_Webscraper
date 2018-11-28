#include <cstdio>
#include <cstring>

using namespace std;

bool seen[10];

int count(long long num) {
  int ans = 0;
  while(num) {
    int digit = num % 10;
    num /= 10;
    if(!seen[digit]) {
      ans++;
    }
    seen[digit] = true;
  }
  return ans;
}

int main() {
  int tc;
  scanf("%d", &tc);
  long long num;
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%lld", &num);
    if(num == 0) {
      printf("Case #%d: INSOMNIA\n", kase);
    } else {
      memset(seen, false, sizeof seen);
      int total = 0;
      long long cur = num;
      while(true) {
	total += count(cur);
	if(total == 10)
	  break;
	cur += num;
      }
      printf("Case #%d: %lld\n", kase, cur);
    }
  }
  return 0;
}
