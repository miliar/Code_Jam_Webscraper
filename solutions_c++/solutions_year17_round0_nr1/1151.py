#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        char str[2000];
        int flip;
        scanf("%s%d", str, &flip);
        
        int i, j;
        int t = 0;
        for (i = 0; i < strlen(str) - flip+1; i++) {
            if (str[i] == '-') {
                t++;
                for (j = 0; j < flip; j++) {
                    if (str[i+j] == '-')
                        str[i+j] = '+';
                    else
                        str[i+j] = '-';
                }
            }
        }
        
        for (i = 0; i < strlen(str); i++)
            if (str[i] == '-')
                break;
        
        if (i != strlen(str)) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        printf("%d\n", t);

    }
}
        