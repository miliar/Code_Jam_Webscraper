#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x);
lli mod = 1000000007;
using namespace std;

int main()
{
    lli t, n, dig[11], i, j, p, x, c, d, p1;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    p = 1;
    cin>>t;
    while(t--) {
        cin>>n;
        for (i = 0; i < 10; i++) {
            dig[i] = 0;
        }
        p1 = n;
        d = 1;
        if (n == 0) {
            cout<<"Case #"<<p<<":"<<" "<<"INSOMNIA"<<endl;
                p++;
        }
        if (n != 0) {
        while(1) {
            c = n;
            while(n > 0) {
                x = n % 10;
                n = n / 10;
                dig[x] = 1;
            }
            int flag = 0;
            for (i = 0; i <= 9; i++) {
                if (dig[i] == 1) {
                } else {
                    d++;
                    n = d * p1;
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                cout<<"Case #"<<p<<":"<<" "<<c<<endl;
                p++;
                goto hell;
                }
            }
        hell:;
        }
    }
    return 0;
}
