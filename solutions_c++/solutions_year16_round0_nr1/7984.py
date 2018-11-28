#include <bits/stdc++.h>

using namespace std;

int main () {
    freopen ("output.txt" , "w" , stdout);
    freopen ("A-large.in" , "r" , stdin);

    int tests;
    cin >> tests;
    for (int t = 1 ; t <= tests ; ++t){
            int n;
            cin >> n;

            cout << "Case #" << t << ": ";
            if (n == 0) {
                    cout << "INSOMNIA\n";
                    continue;
            }
            int used = 0 , cnt = 0 , i = 0;
            while (cnt < 10){
                i ++;
                int p = n * i;
                while (p > 0) {
                        if ( !(used & (1 << (p % 10))) ) {
                                used |= (1 << (p % 10));
                                cnt ++;
                        }
                        p /= 10;
                }
            }
            //cout << used << "\n";
            cout << n * i << "\n";
    }
    return 0;
}
