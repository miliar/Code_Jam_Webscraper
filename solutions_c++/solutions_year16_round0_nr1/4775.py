#include <iostream>
#include <cstring>
#include <cstdlib>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int i, j, k, l, n;
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>n;
    int b[10] =  {0};
    for (i = 1; i <= n; i++) {
        cin>>j;
        memset (b, 0, sizeof(b));
        if (!j) {
            cout<<"Case #"<<i<<": INSOMNIA\n";
            continue;
        }
        long long int cnt = 0;
        for (k = j; ;k+=j) {
            l = k;
            while (l) {
                if (b[l%10] == 0) {
                    b[l%10]++;
                    cnt++;
                }
                l/=10;
            }
            if (cnt == 10) {
                cout<<"Case #"<<i<<": "<<k<<endl;
                break;
            }
        }
    }


    return 0;
}

