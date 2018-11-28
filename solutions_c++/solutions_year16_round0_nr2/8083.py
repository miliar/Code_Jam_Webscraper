#include <bits/stdc++.h>

using namespace std;

int main () {
    freopen ("output.txt" , "w" , stdout);
    freopen ("B-large.in" , "r" , stdin);

    int tests;
    cin >> tests;
    for (int t = 1 ; t <= tests ; ++t){
            int n;
            char now = '-';
            string s;

            cin >> s;
            cout << "Case #" << t << ": ";

            n = (int)s.length();
            int cnt = 0;
            for (int i = n - 1 ; i >= 0 ; --i) {
                    if (s[i] == now) {
                            cnt ++;
                            now = now == '-' ? '+' : '-';
                    }
            }
            cout << cnt << "\n";
    }
    return 0;
}
