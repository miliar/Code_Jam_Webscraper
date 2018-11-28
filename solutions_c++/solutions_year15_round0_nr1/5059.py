#include <cstdio>
using namespace std;

const int maxn = 1<<10;

void run(int test_case) {
  int s_max;
  char num_with_shyness[maxn];
  scanf("%d %s", &s_max, num_with_shyness);
  int num_to_invite = 0;
  int total_standing_until_now = num_with_shyness[0] - '0';
  for (int i = 1; i <= s_max; ++i) {
    if (i > total_standing_until_now) {
      num_to_invite += i - total_standing_until_now;
      total_standing_until_now = i;
    }
    total_standing_until_now += num_with_shyness[i] - '0';
  }
  printf("Case #%d: %d\n", test_case, num_to_invite);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    run(i+1);
  }
  return 0;
}
