#include <iostream>
using namespace std;
int ans = 0;
bool f[2001];
bool work(int x, int k) {
    if (x < k) {
        for (int i = 0; i < x; i++)
            if (!f[i]) return false;
        return true;
    }
    //x >= k
    int j = x;
    for (int i = x-1; i >= x-k; i--)
        f[i] = !f[i];
    ans++;
    while (j > 0 && f[j-1]) j--;
    return work(j, k);
}

int main()
{
    int T, l, k;
    char ch[2001];
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> ch >> k;
        l = int(strlen(ch));
        for (int j = 0; j < l; j++) {
            if (ch[j] == '+') f[j] = true;
            else f[j] = false;
        }
        ans = 0;
        int j = l;
        while (j > 0 && f[j-1]) j--;
        printf("Case #%d: ", i);
        if (work(j, k)) cout << ans << endl;
        else puts("IMPOSSIBLE");
    }
    return 0;
}
