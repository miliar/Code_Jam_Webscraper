#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <iostream>

static double find_minimal_seconds_to_win(double c,
                                          double f,
                                          double x)
{
  double ret = 0.0;
  double income = 2;

    while (1) {
      double time_to_win = x/income;
      double time_to_farm = c/income;
      double time_to_win_next = time_to_farm + x/(income+f);

        if (time_to_win < time_to_win_next) {
            ret += time_to_win;
          break;
        }
        ret += time_to_farm;
        income += f;
    }
  return ret;
}

int32_t main(int32_t argc, char **argv)
{
  int32_t T = 0;
  double c, f, x;

    std :: cin >> T;

    for (int32_t i = 1; i <= T; ++i) {
        std :: cin >> c >> f >> x;

        fprintf(stdout, "Case #%d: %.7lf\n",
                i, find_minimal_seconds_to_win(c, f, x));
    }
  return 0;
}
