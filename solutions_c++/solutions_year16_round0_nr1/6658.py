#include <cstdio>
#include <iostream>

using namespace std;

int T, tmp, last, N;
long long now;
bool vis[101];

int main()
{
    freopen("A_small.in", "r", stdin);
    freopen("A_small.out", "w", stdout);

    cin >> T;

    for (int Cas = 1; Cas <= T; ++Cas) {
        cout << "Case #" << Cas << ": ";

        cin >> N;

        if (N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        tmp = 10;
        for (int i = 0; i <= 9; ++i) vis[i] = false;

        for (int i = 1; i <= 10101010; ++i) {
            now = (long long)N * i;
            while (now) {
                last = now % 10;
                if (!vis[last]) {
                    vis[last] = true;
                    -- tmp;
                }
                now /= 10;
            }
            if (!tmp) {
                cout << N * i;
                break;
            }
        }

        cout << endl;
    }

    return 0;
}
