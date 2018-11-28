#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int T; cin >> T;
    for(int t = 0; t < T; ++t) {
        double c, f, x;
        cin >> c >> f >> x;

        double p = 2;
        double ti = 0;

        while(x/p > c/p + x/(p+f)) {
            ti += c/p;
            p += f;
        }

        ti += x/p;
        printf("Case #%d: %.7f\n", t+1, ti);
    }

    return 0;
}
