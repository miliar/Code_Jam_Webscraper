#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>

#define PII pair<int, int>

using namespace std;

int main(){
    
    int t, i;
    scanf("%d", &t);
    double a, b, y1, y2, c, f, x;
    for(int z = 1; z <= t; z++){
        scanf("%lf %lf %lf", &c, &f, &x);
        y1 = x/2;
        y2 = c/2 + x/(f+2);
        i = 1;
        while(y2 < y1){
            y1 = y2;
            y2 = y2 + c/(2 + i*f) - x/(2 + i*f) + x/(2 + i*f + f);
            i++;
        }
        printf("Case #%d: %.7lf\n", z, y1);
    }

    return 0;
}
