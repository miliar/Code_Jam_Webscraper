#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

int n;

void solve()
{
    if (n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }
    vector<int8_t> cnt(10, 0);

    int last = 10;
    int q = 1;
    while (last > 0) {
        int m = n * q;
        while (m) {
            if (cnt[m % 10] == 0) {
                cnt[m % 10]++;
                last--;
            }
            m /= 10;
        }
        if (last > 0) {
            q++;
        }
    }
    cout << n * q << endl;
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}