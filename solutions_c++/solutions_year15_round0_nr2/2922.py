#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;
    cin >> cases;

    for (int test = 1; test <= cases; test++) {
        int d;
        cin >> d;

        vector<int> p(d);

        int pmax = 0;
        for (auto& e : p) {
            cin >> e;
            pmax = max(pmax, e);
        }

        int t = pmax;
        for (int i = 1; i <= pmax; i++) {
            int sm = 0;

            for (auto e : p) {
                sm += e / i - 1;

                if (e % i) {
                    sm++;
                }
            }

            t = min(t, sm + i);
        }

        cout << "Case #" << test << ": " << t << endl;
    }
}