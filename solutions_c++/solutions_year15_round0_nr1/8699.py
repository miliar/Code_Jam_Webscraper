#include <cstdio>

int main (int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for (int i=0; i<T; i++) {
        int Smax;
        char S[1002];
        scanf("%d %s", &Smax, S);

        int nStand = S[0] - '0';
        int required = 0;
        for (int j=1; j<=Smax; j++) {
            int n = S[j] - '0';
            
            if (n == 0)
                continue;

            if (j <= nStand) {
                nStand += n;
            } else {
                int missing = j - nStand;
                required += missing; 
                nStand += missing + n;
            }
        }

        printf("Case #%d: %d\n", i+1, required);
        
    }
    
    return 0;
}
