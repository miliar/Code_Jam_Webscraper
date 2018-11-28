#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <utility>
#include <string>
#include <map>
#include <set>

using namespace std;
const int MAXN = 1000000;

int t;
long double c, f, x, F;
long double act, left;

int main() {
    scanf("%d", &t);
    for(int fi = 1; fi <= t; ++fi) {
        scanf("%Lf %Lf %Lf", &c, &f, &x);
        F = 2.0;
        left = 0.0;
        while(1) {
            long double one = left + x / F;
            long double two = left + c / F + x / (F + f);
            if(one < two) {
                left = one;
                break;
            }
            left += c / F;
            F += f;
        }
        printf("Case #%d: %.7Lf\n", fi, left);
    }    
    return 0;
}
