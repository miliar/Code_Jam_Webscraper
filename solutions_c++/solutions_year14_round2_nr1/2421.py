#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int process(string& a, string& b, int* blocksa, int* blocksb)
{
    char blocks[a.length()];
    char x = a[0];
    int breaks = 0;
    int len = 0;
    for (char c : a + "!") {
        if (c == x) {
            ++len;
            continue;
        }
        blocks[breaks] = x;
        blocksa[breaks++] = len;
        x = c;
        len = 1;
    }

    len = 0;
    x = b[0];
    int breaks2 = 0;
    for (char c : b + "!") {
        if (c == x) {
            ++len;
            continue;
        }

        if (blocks[breaks2] != x)
            return -1;
        if (breaks2 > breaks)
            return -1;

        blocksb[breaks2++] = len;
        x = c;
        len = 1;
    }

    if (breaks != breaks2)
        return -1;

    return breaks;
}

int solve(int a, int b)
{
    return abs(a - b);
}

void solve(string& sa, string& sb)
{
    int a[sa.length()], b[sb.length()];
    int n = process(sa, sb, a, b);
    if (n == -1) {
        cout << "Fegla Won" << endl;
        return;
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += solve(a[i], b[i]);
        // printf("a[%d] = %d\nb[%d] = %d\n\n", i, a[i], i, b[i]);
    }

    cout << ans << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        int N;
        cin >> N;
        assert(N == 2);
        string sa, sb;
        cin >> sa;
        cin >> sb;
        printf("Case #%d: ", i);
        solve(sa, sb);
    }
    return 0;
}

