#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

double c,f,x;

int main () {
    freopen("test.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    cin >> t;
    for( int tc=1; tc<=t; tc++ ) {
        cin >> c >> f >> x;
        cout << "Case #" << tc << ": ";
        double acum = 0.0;
        int k = 0;
        while ( c/(k*f+2) + x/(f*(k+1)+2) < x/(f*k+2) ) {
            acum += c/(k*f+2);
            k++;
        }
        acum += x/(f*k+2);
        printf("%.7lf\n",acum);

    }
    return 0;
}
