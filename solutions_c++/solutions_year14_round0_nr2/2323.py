#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <list>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cmath>
using namespace std;

double k[100000000], b[100000000];

int main()
{
    k[0] = 2.0;
    b[0] = 0.0;
    int T;
    double C, F, X, min, time, end, k, pk, base;
    const double eps = 1e-12;
    scanf("%d", &T);
    
    for (int tot = 1; tot <= T; tot++) {
        scanf("%lf%lf%lf", &C, &F, &X);
        pk = k = 2.0;        
        min = end = X / pk;
        base = C/pk;

        while (base <= end) {
            k = pk+F;
//            printf("k = %f, pk = %f, base = %f, end = %f, time = %f\n", k, pk, base, end, time);
            time = base + X/k;
            if (time < min) { min = time;
                //              printf("min = %f\n", min);
            }
            base += C/k;
            if (base > min) break;
            //if (C/k < eps) break;
            
            pk = k;
        }
        
        
        printf("Case #%d: ", tot);
        printf("%.7f\n", min);
    }
    return 0;
}
