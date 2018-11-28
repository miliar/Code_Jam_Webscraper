#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("ovation.in", "r", stdin);
    freopen("ovation.out", "w", stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int K;
        cin >> K;
        string a;
        cin >> a;
        int kiek_stovi = 0;
        int papild = 0;
        for (int k = 0; k <= K; k++) {

            int b = a[k] - '0';
            if (a[k] != '0') {
                if (k > kiek_stovi) {
                    papild += k - kiek_stovi;
                    kiek_stovi += k - kiek_stovi;
                }
                kiek_stovi += b;
            }
        }
        cout << "Case #" << i + 1 << ": " << papild << endl;
    }
    return 0;
}
