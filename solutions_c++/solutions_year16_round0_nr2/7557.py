#include <stdio.h>
#include <string.h>
char S[150];
long long solve () {
    int i;
    long long int count = 0;
    for (i = strlen(S)-1; i >= 0; i--) {
        if ((count%2==0 && S[i]=='-') || (count%2==1 && S[i]=='+')) {
            count++;
        }
    }
    return count;
}
int main () {
    int T;
    int i;
    scanf("%d", &T);
    for (i = 1; i <= T; i++) {
        scanf("%s", S);
        printf("Case #%d: %lld\n", i, solve());
    }
}
