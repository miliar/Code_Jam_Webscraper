#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>

static bool happy_stack(const std::string &str)
{
  return !std::any_of(str.begin(), str.end(),
                      [&](const char c) { return c == '-'; });
}

static int32_t min_maneuvers(std::string &str)
{
  int32_t ret = 0;
  int32_t last_unhappy = str.length()-1;

    while (!happy_stack(str)) {
        if (str[0] == '+') {
            // reverse first +++ to --, so later they will become ++ again
          int32_t e = 0;
            for (e = 1; e < last_unhappy; ++e) {
                if (str[e] == '-') {
                  break;
                }
            }
            for (int32_t i = 0; i < e; ++i) {
                str[i] = '-';
            }
            ++ret;
#if DEBUG > 1
            fprintf(stdout, "str = %s; ret = %d\n", str.c_str(), ret);
#endif // DEBUG > 1
        }

        for (; last_unhappy >= 0; --last_unhappy) {
            if (str[last_unhappy] == '-') {
              break;
            }
        }

        // perform maneuver
        std::reverse(str.begin(), str.begin()+last_unhappy+1);
        for (int32_t i = 0; i <= last_unhappy; ++i) {
            str[i] = str[i] == '-' ? '+' : '-';
        }
        ++ret;
#if DEBUG > 1
        fprintf(stdout, "str = %s; ret = %d\n", str.c_str(), ret);
#endif // DEBUG > 1
    }
  return ret;
}

int32_t main(int32_t argc, char **argv)
{
  int32_t t;
    std::cin >> t;
    for (int32_t i = 1; i <= t; ++i) {
      std::string str;
        std::cin >> str;
        fprintf(stdout, "Case #%d: %d\n", i, min_maneuvers(str));
    }
  return 0;
}
