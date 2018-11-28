#include <iostream>
#include <algorithm>

using namespace std;

int a[1001];
int T, e, D, x;

bool bisakah(int m)
{
    for (int i = 1; i <= m; ++i) {
        x = i;
        for (int j = 0; j < D; ++j) {
            x += (a[j] - 1) / i;
            if (x > m)
                break;
        }
        if (x <= m)
            return true;
    }

    return false;
}

int coba(int l, int r)
{
    if (l >= r)
        return l;

    int m = (l + r) >> 1;
    if (bisakah(m))
        return coba(l, m);
    else
        return coba(m + 1, r);
}

int main()
{
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> D;

        for (int j = 0; j < D; ++j) {
            cin >> x;
            a[j] = x;
        }

        sort(a, a + D);

        cout << "Case #" << i << ": " << coba(0, a[D - 1]) << endl;
    }
    return 0;
}