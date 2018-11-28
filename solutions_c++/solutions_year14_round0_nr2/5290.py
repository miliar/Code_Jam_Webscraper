#include <bits/stdc++.h>

using namespace std;


double findTime (double c, double f, double x, int buy) {
      if (buy == 0) return 0;
      double ans = 0.0;
      ans += c / 2.0;
      buy --;
      for (int i = 0; i < buy; i++) {
            ans += c / (2.0 + (i + 1) * f);
      }
      return ans;
}

double getTime (double c, double f, double x, int buy) {
      double rate = 2 + buy * f;
      double timeTaken = findTime (c, f, x, buy);

      return timeTaken + x / rate;
}


int main() {
      freopen ("input.txt", "r", stdin);
      freopen ("output1.txt", "w", stdout);


      int T, caseNo = 1;
      cin >> T;

      while (T--) {
            cout << "Case #" << caseNo ++ << ": ";


            double c, f, x, ans = 0;
            cin >> c >> f >> x;
            //cout << c << "  " << f <<  " " << x << endl;

            if (x <= c) ans = x / 2.0;
            else {
                  ans = 1e18;

                  for (int buy = 0; buy <= (int) 100; buy++) {
                        double rate = 2 + buy * f;
                        double timeTaken = findTime (c, f, x, buy);
                        //cout << buy << " " << timeTaken << " " << rate << endl;
                        //cout << timeTaken + x / rate << endl;
                        ans = min (ans, timeTaken + x / rate);
                  }

                  for (int buy = max (0, (int) x - 100); buy <= (int) x + 100; buy++) {
                        double rate = 2 + buy * f;
                        double timeTaken = findTime (c, f, x, buy);
                        //cout << buy << " " << timeTaken << " " << rate << endl;
                        //cout << timeTaken + x / rate << endl;
                        ans = min (ans, timeTaken + x / rate);
                  }

                  int lo = 0, hi = (int) x + 20000;
                  for (int it = 0; it < 100; it++) {
                        int mid1 = (lo + (hi - lo) / 3);
                        int mid2 = (hi - (hi - lo) / 3);

                        //cout << lo << " " << hi << endl;
                        //cout << mid1 << " " << mid2 << endl;

                        if (getTime (c, f, x, mid1) < getTime (c, f, x, mid2)) {
                              hi = mid2;
                        } else lo = mid1;

                        ans = min (ans, getTime (c, f, x, mid1));
                        ans = min (ans, getTime (c, f, x, mid2));
                  }

                  //cout << ans << endl;
            }

            cout << setprecision(20) << ans << endl;
            //printf ("%.7lf\n", ans);

            //assert (false);
      }

      return 0;
}
