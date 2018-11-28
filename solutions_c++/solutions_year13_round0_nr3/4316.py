#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef long long i64;

const i64 MAXN=10000000L;
//const i64 MAXN=100L;

i64 nums[MAXN];
i64 total = 0;

bool is_palin(i64 n) {
  char buff[32]; sprintf(buff, "%lld", n);
  int len = strlen(buff);
  for(int i=0; i<len/2; ++i) 
    if(buff[i] != buff[len-i-1]) return false;
  return true;
}

void init() {
  for(i64 i=1L; i<=MAXN; ++i) {
    if(is_palin(i) && is_palin(i*i)) {
      nums[total++]=i*i;// printf("nums[%lld] = %lld\n", total-1, nums[total-1]);
    }
  }
}

i64 answer(i64 A, i64 B) {
  return upper_bound(nums, nums+total, B)-lower_bound(nums, nums+total, A);
}

int main() {
  init();
  int T; scanf("%d", &T);
  for(int ic=1; ic<=T; ++ic) {
    i64 A, B; scanf("%lld %lld", &A, &B);
    printf("Case #%d: %lld\n", ic, answer(A, B));
  }
  return 0;
}
