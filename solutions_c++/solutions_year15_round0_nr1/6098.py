#include <iostream>
#include <cstdio>

using namespace std;

const int maxn = 1e5 + 100;

int t, k, cnt, sum;
char ch[maxn];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a.txt", "w", stdout);
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> k;
        scanf("%s", ch);
        cnt = 0, sum = (ch[0] - '0');
        for (int j = 1; j < k + 1; ++j) {
            if (ch[j] != '0') {
                if (cnt + sum < j) cnt += j - sum - cnt;
                sum += (ch[j] - '0');
            }
        }
        cout << "Case #" << i + 1 << ": " << cnt << endl;
    }
    return 0;
}
