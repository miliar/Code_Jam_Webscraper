#include <iostream>
#include <string>

using namespace std;

#define FILENAME "A-large.in"

void solve() {
    int smax;
    int already = 0;
    int need = 0;
    string s;
    cin >> smax;
    cin >> s;

    for (int i = 0; i <= smax; i ++) {
        int this_lv = s[i] - '0';
        if (!this_lv) {
            continue;
        }

        if (i > already) {
            need += i - already;
            already = i;
        }

        already += this_lv;
    }

    cout << need;
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

