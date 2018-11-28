#include <bits/stdc++.h>

using namespace std;

int n;

string solve() {
    cin >> n;
    if (n == 0) return "INSOMNIA";
    int m = n;
    bool ok[10];
    for(int i = 0; i < 10; i++) ok[i] = false;
    for(int i = 0; i < to_string(m).length(); i++) ok[int(to_string(m)[i]) - 48] = true;

    bool done = true;
    for(int i = 0; i < 10; i++)
        if (!ok[i]) {
            done = false;
            break;
        }

    while (!done) {
        m += n;
        for(int i = 0; i < to_string(m).length(); i++) ok[(int)(to_string(m)[i]) - 48] = true;
        done = true;
        for(int i = 0; i < 10; i++)
            if (!ok[i]) {
                done = false;
                break;
            }
    }

    return to_string(m);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int tests;
    cin >> tests;
    for(int tc = 1; tc <= tests; tc++) {
        cout << "Case #" << tc << ": " << solve() << endl;
    }
}
