#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int lli;

const int maxn = 10000000;
const int maxs = 20;
char str[maxs];

bool isPal(lli number) {
    int i, n;

    sprintf(str, "%lld", number);

    n = strlen(str);
    for (i = 0; i < (n >> 1); i++) {
        if (str[i] != str[n - i - 1]) {
            return false;
        }
    }

    return true;
}

int main() {
    int t, tt, i, n;
    lli a, b, tmp;
    vector<lli> ans;
    vector<lli>::iterator it1, it2;

    for (i = 1; i <= maxn; i++) {
        tmp = (lli) i * (lli) i;
        if (isPal(tmp) && isPal((lli) i)) {
            ans.push_back(tmp);
        }
    }

    cin >> t;
    for (tt = 1; tt <= t; tt++) {
        cin >> a >> b;

        it1 = lower_bound(ans.begin(), ans.end(), a);
        it2 = upper_bound(ans.begin(), ans.end(), b) - 1;

        n = max((int) (it2 - it1 + 1), 0);

        cout << "Case #" << tt << ": " << n << endl;
    }

    return 0;
}
