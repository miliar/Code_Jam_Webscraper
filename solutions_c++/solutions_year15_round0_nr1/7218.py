#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <tuple>
#include <algorithm>
#include <utility>
#include <iostream>
#include <complex>
#include <exception>

static int32_t find_solution(const int32_t s,
                             const std :: string &str)
{
  int32_t ret = 0;
  int32_t stand = 0;
    for (int32_t i = 0; i < str.length(); ++i) {
        if (str[i] != '0') {
            if (stand >= i) {
                stand += str[i] - '0';
            }
            else {
                ret += i-stand;
                stand = i + (str[i] - '0');
            }
        }
    }
  return ret;
}

int32_t main(int32_t argc, char **argv)
{
  int32_t t;
  int32_t s;
    std :: cin >> t;

    for (int32_t i = 0; i < t; ++i) {
      std :: string str;
        std :: cin >> s;
        std :: cin >> str;
        fprintf(stdout, "Case #%d: %d\n", i+1, find_solution(s, str));
    }
  return 0;
}
