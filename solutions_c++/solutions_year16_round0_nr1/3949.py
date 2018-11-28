#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long int
#define s(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define sd(x) scanf("%lf", &x)
#define mod 1000000007
#define get getchar_unlocked

int mrk[11];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("CJO1.txt", "w", stdout);
    int t, n, j, cnt, k, u = 0;
    cin >> t;
    while (t--) {
        cin >> n;
        printf("Case #%d: ", ++u);
        if (!n) {
            printf("INSOMNIA\n");
            continue;
        }
        memset(mrk, 0, sizeof(mrk));
        j = 0;
        cnt = 0;
        while (cnt < 10) {
            j += n;
            k = j;
            while (k) {
                if (!mrk[k%10]) {
                    mrk[k%10] = 1;
                    ++cnt;
                }
                k /= 10;
            }
        }
        printf("%d\n", j);
    }
    return 0;
}
