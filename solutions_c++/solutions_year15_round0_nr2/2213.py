#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define FILENAME "B-large.in"

void solve() {
    int D, n;
    int max = 0;
    vector<int> p;

    cin >> D;
    n = D;
    while(D--) {
        int pancakes;
        cin >> pancakes;
        p.push_back(pancakes);
        if (pancakes > max) {
            max = pancakes;
        }
    }

    int best_case = 1000;
    do {
        int c = max;
        for (int i = 0; i < p.size(); i++) {
            int pp = p[i];
            c += pp / max - (!(pp % max));
        }
        if (c < best_case) {
            best_case = c;
        }
    } while (--max);

    cout << best_case;
}

int main()
{
    freopen("E:\\contest\\" FILENAME, "r", stdin);
    freopen("E:\\contest\\output", "w", stdout );

    int cases = 0, T;
    cin >> T;

    while (T--) {
        cout << "Case #" << ++cases << ": ";
        solve();

        cout << endl;
    }


    return 0;
}

