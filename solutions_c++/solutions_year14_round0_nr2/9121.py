#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
int main() {
    int t;
    cin>>t;
    for (int ncase = 1; ncase <= t; ncase++) {
        double c,f,x;
        cin>>c>>f>>x;
        double result = x / 2;
        double tmpresult = 0;
        double rate = 2;
        for (int i = 0; ;i++) {
            tmpresult += c / rate;
            rate += f;
            double tmp = tmpresult + x / rate;
            if (tmp < result)
                result = tmp;
            else
                break;
        }
        printf("Case #%d: %.7lf\n", ncase, result);
    }
    return 0;
}
