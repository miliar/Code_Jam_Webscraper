// in the name of ogd

#include <bits/stdc++.h>

using namespace std;
bool vis[1000];
int32_t main() {
    int t; cin >> t;
   // int o = 0;
    for (int tt = 1; tt <= t; tt++) {
        int x; cin >> x;
        memset(vis, 0, sizeof vis);
      //  bool f = 0;
        if (x == 0) {
          cout << "Case #" << tt << ": " << "INSOMNIA" << endl;
        }
        for (int i = 1; i <= 200; i++) {
            int xx = x * i;
            while(xx) {
                vis[xx%10]++;
                xx /= 10;
            }
            bool g = 0;
            for (int j = 0; j < 10; j++)
                if(!vis[j])
                    g = 1;
            if (!g) {
          //      f = 1;
                // cout << '*' << x << endl;
              //  o++;
                cout << "Case #" << tt << ": " << x*i << endl;
                break;
            }
        }
      //  if(f == 0)
        //    cout << x << endl;
    }
}