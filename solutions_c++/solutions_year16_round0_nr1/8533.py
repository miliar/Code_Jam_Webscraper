#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>

#define LL8 100000000

using namespace std;

typedef unsigned long long ll;

int t, tc, n;
bool digit[11];

int main()
{
    
    scanf("%d", &tc);
    
    n = 0;
    for (int t=1; t<=tc; t++) {
        scanf("%d", &n);
        
        printf("Case #%d: ", t);
        
        memset(digit, 0, sizeof(digit));
        
        int sum = 0;
        if (n == 0)
            printf("INSOMNIA\n");
        else {
            unsigned long long cn = 0, x;
            while (sum != 55) {
                cn += n;
                x = cn;
                while (x > 0) {
                    if (!digit[x % 10]) {
                        digit[x % 10] = true;
                        sum += (x % 10 + 1);
                    }
                    x /= 10;
                }
            }
            
            printf("%d\n", cn);
        }
        
    }
    
    return 0;
}