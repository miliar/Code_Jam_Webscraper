#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    long int z, p;
    cin >> z;
    p = 1;
    while(z != 0) {
    long int i, j, n, m = 0, t = 0;
    cin >> n;
    long double a[n], b[n];

    for(i = 0; i < n; i++) {
        cin >> a[i];
    }
    for(i = 0; i < n; i++) {
        cin >> b[i];
    }
    sort(a, a+n);
    sort(b, b+n);
    j = n - 1;
    for(i = n - 1; i >= 0; i--) {
            if(a[i] < b[j]) {
                j--;
                m++;
            }
    }
    i = n - 1;
    for(j = n - 1; j >= 0; j--) {
            if(a[i] < b[j]) {
                t++;
            }
            else{
                i--;
            }
    }
    cout <<"Case #"<< p << ": " << n - t << " " << n - m << endl;
    z--;
    p++;
    }
    return 0;
}
