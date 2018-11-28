#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;

bool checked(int64 i) {
    int l = 0;
    int a[30];
    memset(a, 0, sizeof(a));
    while (i) {
        a[l] = i % 10;
        l++;
        i /= 10;
    }
    for (int j = 0; j < (l + 1) / 2; j++) {
        if (a[j] != a[l - j - 1])
            return false;
    }
    return true;
}

int main() {
    freopen("d://in.txt", "r", stdin);
    freopen("d://out.txt", "w", stdout);

    vector<int64> vec;
    vec.clear();

    for (int64 i = 1; i <= 100000000l; i++) {
        if (checked(i) && checked(i * i))
            vec.push_back(i * i);
    }

    int t;
    scanf("%d", &t);
    for (int ti = 1; ti <= t; ti++) {
        int64 n, m;
        scanf("%lld %lld", &n, &m);
        vector<int64>::iterator low, up;
        low = lower_bound(vec.begin(), vec.end(), n);
        up = upper_bound(vec.begin(), vec.end(), m);
        cout << "Case #" << ti << ": " << (up - low) << endl;
    }

    return 0;
}
