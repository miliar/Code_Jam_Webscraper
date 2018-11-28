#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

typedef long long int int64;

vector <int64> ans;

void gen(int64 genc)
{
    ans.resize(genc + 1);
    ans[0] = -1;
    for (int64 i = 1; i <= genc; ++i) {
        int64 symbols = 0;
        int64 j;
        vector <int64> m(10, 0);
        for (j = 1; symbols < 10; ++j) {
            int64 var = i * j;
            while (var > 9) {
                m[var % 10] = 1;
                var /= 10;
            }
            m[var] = 1;
            symbols = 0;
            for (int k = 0; k < 10; ++k) {
                symbols += m[k];
            }
            if (j > 1000000) {
                exit(-1);
            }
        }
        ans[i] = i * (j - 1);
    }
}

int main()
{
    int t;
    cin >> t;
    gen(2000000);
    for (int i = 1; i <= t; ++i) {
        int val;
        cin >> val;
        cout << "Case #" << i << ": " ;
        if (ans[val] != -1) {
            cout << ans[val] << "\n";
        } else {
            cout << "INSOMNIA\n";
        }
    }

    return 0;
}

