#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("inl.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,p = 0;
    cin >> t;
    double c,f,x,r = 2,sum;
    while (t--) {
        r = 2;
        cin >> c >> f >> x;
        sum = 0;
        while (1) {
            if ((c/r)+(x/(r+f)) >= (x/r)) {
                sum += x/r;
                break;
            }
            else {
                sum += c/r;
                r += f;
            }
        }
        printf("Case #%d: %.7lf\n", ++p, sum);
    }
    return 0;
}
