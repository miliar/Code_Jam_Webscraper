
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

typedef std::pair<uint64_t, uint64_t> long_t;
const uint64_t part_max = ((uint64_t)1 << 58);

long_t plus_long(const long_t& l, const long_t& r) {
  long_t res = {0, 0};
  res.first = l.first + r.first;
  if (res.first >= part_max) {
    res.second += res.first / part_max;
    res.first = res.first % part_max;
  }
  res.second += l.second + r.second;
  return res;
}

long_t mul_long(const long_t& l, unsigned val) {
  long_t res = l;
  res.first *= val;
  res.second *= val;
  if (res.first >= part_max) {
    res.second += res.first / part_max;
    res.first = res.first % part_max;
  }
  return res;
}

uint64_t calc_mod(const long_t& val, uint64_t m) {
  uint64_t first = val.first % m;
  uint64_t second = ((val.second % m) * (part_max % m)) % m;
  return (first + second) % m;
}

uint64_t find_div(const long_t& val, unsigned base) {
  if (calc_mod(val, 3) == 0) {
    return 3;
  }
  uint64_t cur = 5;
  const uint64_t maxcur = 1 << 20;
  while (cur < maxcur) {
    if (calc_mod(val, cur) == 0) {
      return cur;
    }
    if (calc_mod(val, cur+2) == 0) {
      return cur+2;
    }
    cur += 6;
  }
  return 1;
}

long_t convert(unsigned val, unsigned base) {
  long_t res = {0, 0};
  long_t mul = {1, 0};
  while (val) {
    if (val & 1) {
      res = plus_long(res, mul);
    }
    val >>= 1;
    mul = mul_long(mul, base);
  }
  return res;
}

void to_bin(unsigned val, char* buff) {
  char* cur = buff;
  while (val) {
    *cur = (val & 1) ? '1' : '0';
    val >>= 1;
    ++cur;
  }
  *cur = 0;
  --cur;
  while (cur > buff) {
    swap(*cur, *buff);
    --cur;
    ++buff;
  }
}

void solve(int casenum) {
  printf("Case #%d:\n", casenum);
  int n = 0;
  int j = 0;
  std::cin >> n;
  std::cin >> j;
  unsigned cur = (1 << (n-1)) + 1;
  do {
    bool has_prime = false;
    for (unsigned base = 2; base <= 10; ++base) {
      long_t val = convert(cur, base);
      if (find_div(val, base) == 1) {
        has_prime = true;
        break;
      }
    }
    if (!has_prime) {
      char buff[50];
      to_bin(cur, buff);
      printf("%s ", buff);
      for (unsigned base = 2; base <= 10; ++base) {
        long_t val = convert(cur, base);
        uint64_t div = find_div(val, base);
        printf("%llu", div);
        if (base != 10) {
          printf(" ");
        }
      }
      --j;
      printf("\n");
    }
    cur += 2;
  } while (j > 0);
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
