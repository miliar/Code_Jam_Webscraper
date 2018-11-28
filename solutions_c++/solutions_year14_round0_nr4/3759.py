#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
    freopen("inl.in", "r", stdin);
    freopen("outl.txt", "w", stdout);
    int t,n,i,u = 0,p,o,s,e,sa,sb;
    cin >> t;
    while (t--) {
        cin >> n;
        double a[n],b[n];
        for (i = 0; i < n; i++)
            cin >> a[i];
        for (i = 0; i < n; i++)
            cin >> b[i];
        sort(a,a+n);
        sort(b,b+n);
        sa = 0;e = n-1;sb = 0;
        o = 0;
        for (i = n-1; i >= 0; i--) {
            if (a[e] > b[i]) {
                e--;
                o++;
            }
        }
        p = 0;
        s = 0;e = n-1;
        for (i = n-1; i >= 0; i--) {
            if (a[i] > b[e]) {
                s++;
                p++;
            }
            else
                e--;
        }
        u++;
        cout << "Case #" << u << ": " << o << " " << p << endl;
    }
}
