#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int
main()
{
  double C, F, X, lastTime, time, lastFarm, cookies;
  int T, t;
  cin >> T;
  for (t = 1; t <= T; t++) {
    cin >> C >> F >> X;
    lastTime = (X/2);
    lastFarm = 0;
    cookies = 2;
    while (1) {
      lastFarm += C/cookies;
      cookies += F;
      time = lastFarm + X/cookies;
      if (time > lastTime)
        break;
      lastTime = time;
    }

    printf("Case #%d: ", t);
    printf("%.7lf\n", lastTime);
  }


}
