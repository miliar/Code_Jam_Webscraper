#include <bits/stdc++.h>

using namespace std;
typedef long long Long;


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    Long N;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": " ;
        cin >> N;
        if (N == 0) {
            cout << "INSOMNIA";
        } else {
            Long n = 0;
            set<int> d;
            for (int i = 1; i <= 10000; ++i) {
                n = N * Long(i);
                while (n > 0) {
                    d.insert(n % 10);
                    n /= 10;
                }
                if (d.size() == 10) {
                    cout << i * N;
                    n = -1;
                    break;
                }
            }
            if (n > -1) {
                cout << "INSOMNIA";
            }
        }
        cout << "\n";
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
