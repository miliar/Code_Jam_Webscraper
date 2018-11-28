#include <bits/stdc++.h>

using namespace std;

#define s(x) scanf("%d", &x)
#define ll long long

int a[11];

int check()
{
    for (int i = 0; i < 10; i++) {
        if (a[i] == 0)
            return 0;
    }
    return 1;
}

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, z = 1;
    s(t);

    while (t--) {
        int n, f = 0, i, x;
        s(n);

        ll tmp;
        memset(a, 0, sizeof(a));


        for (i = 1; i <= 100000; i++) {
            tmp = (ll)i * (ll)n;
            while (tmp != 0) {
                x = tmp%10;
                tmp /= 10;
                a[x] = 1;
            }

            if(check()) {
                f = 1;
                break;
            }
        }

        printf("Case #%d: ", z++);

        if (!f)
            cout << "INSOMNIA\n";
        else
            cout << ((ll)i * (ll)n) << endl;
    }

    return 0;
}
