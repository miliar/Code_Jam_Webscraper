#include <bits/stdc++.h>

using namespace  std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("2.txt", "w", stdout);

    vector <int> ans(1000010);
    for (int i = 1; i <= 1000000; i++) {
        int mask = 0;
        for (int j = i; ; j += i) {
            int num = j;
            while (num) {
                mask |= (1<<(num%10));
                num /= 10;
            }
            if (mask == 1023) {
                ans[i] = j;
                break;
            }
        }
    }

    int t;
    cin >> t;

    for (int cs = 0; cs < t; cs++) {
        int n;
        cin >> n;
        cout << "Case #" << cs + 1 << ": ";
        if (!n) cout << "INSOMNIA" << endl;
        else cout << ans[n] << endl;
    }

    return 0;
}


