#pragma warning( disable : 4996 ) 
#include <cstdio>
#include <iostream>

using namespace std;


int main(){
    int cc, tt;
    scanf("%d", &tt);
    for (int cc = 1; cc <= tt; cc++){
        double c, fnow=2, f, x, t = 0;
        cin >> c >> f >> x;
        while ((x - c)*(fnow + f) > x*fnow){
            t += c / fnow;
            fnow += f;
        }
        t += x / fnow;
        printf("Case #%d: %.7lf\n", cc, t);
    }
}