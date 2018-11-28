#include <stdio.h>

#define SMAX 1001
char S[SMAX];

int main(){
    int T, n;
    scanf("%d", &T);
    for(int i=1;i<=T;i++){
        scanf("%d %s", &n, S);
        int count = int(S[0]) - '0';
        int res = 0;
        if (!count){
            count++, res++;
        }
        for(int j=1;j<=n;j++){
            if(count<j) {
                res+=j-count;
                count+=j-count;;
            }
            count += int(S[j]) - '0';
        }
        printf("Case #%d: %d\n", i, res);
    }

    return 0;
}
