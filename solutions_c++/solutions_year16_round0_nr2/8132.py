#include <stdio.h>
#include <string.h>

char S[111];
int main() {
    int T; scanf ("%d",&T); for (int test = 1; test <= T; test ++ ) {
        scanf ("\n%s", S+1);
        int N = (int) strlen(S+1);
        int ans = 0;
        for (int i=N;i>=1;i--) {
            if (S[i] == '-') {
                int k = -1;
                for (int j=1;j<i;j++) {
                    if (S[j] == '-') break;
                    S[j] = '-';
                    k = j;
                }
                if (k != -1) ans ++;
                
                for (int j=1;j<=i;j++) {
                    if (S[j] == '+') S[j] = '-';
                    else S[j] = '+';
                }
                
                for (int j=1;j<=i/2;j++) {
                    char a = S[j]; char b = S[i-j+1];
                    S[i-j+1] = a; S[j] = b;
                }
                ans ++;
            }
        }
        printf ("Case #%d: %d\n",test, ans);
        
    }
    return 0;
}
