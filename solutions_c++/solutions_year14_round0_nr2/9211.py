#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int main(){
    int nc;
    scanf("%d", &nc);
    
    for(int caso = 1; caso <= nc; caso++){
    
        double a1, b1, c1;
        scanf("%lf%lf%lf", &a1, &b1, &c1);
        
        long double c, f, x;
        c = a1, f = b1, x = c1;
        long double aux = x/c - 2/f - 1.0;
        int r = (int)ceil(aux);
        if(r < 0) r = 0;
        
        long double ac = 0, fac = 2, res = x/2;
        for(int i = 0; i <= r + 3; i++){
            if(res > ac + x/fac) res = ac + x/fac;
            ac += c/fac;
            fac += f;
        }
        
        printf("Case #%d: %.7lf\n", caso, (double)res);
        
    }
}
