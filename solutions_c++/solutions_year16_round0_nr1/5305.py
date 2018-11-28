/** CyCraig33 - Google Code Jam 2016 Qualification Problem A**/
#include <cstdio>
#include <cstring>

// accepted

// still has some weird bug where it needs an extra input at the end

bool digits[10];

int main(void) {
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    
    int n,c = 0;
    unsigned long long N;
    scanf("%d\n",&n);
    for(int l = 0; l < n; l++) {
        memset(digits,0,sizeof(digits));
        scanf("%d\n",&N);
        bool found = false;
        for(int i = 1; i <= 100 && !found; i++) {
            
            // decompose digits
            unsigned long long temp = N*i;
            do {
                int digit = temp % 10;
                digits[digit] = true;
                temp /= 10;
            } while (temp > 0);
            
            // check digits
            bool asleep = true;
            for(int j = 0; j < 10 && asleep; j++) {
                asleep = digits[j];
            }
            
            found = asleep;
            if( found ) printf("Case #%d: %d\n",++c,N*i);
        }
        
        if( !found ) printf("Case #%d: INSOMNIA\n",++c);
    }
    fflush(stdout);
    
    
    return 0;
}