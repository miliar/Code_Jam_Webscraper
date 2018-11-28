#include <stdio.h>
#include <string.h>
#include <algorithm>
int min(int a, int b){ return a < b?a:b; }
char str[2010];
char base[][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int order[] = {0, 2, 4, 6, 5, 7, 8, 1,9, 3};
char identifier[] = "ZWUXFVGOIT";
int bucket[200];
char output[2010];
void solve(int c){
    int olen = 0;
    printf("Case #%d: ", c);
    memset(bucket, 0, sizeof(bucket));
    int len;
    int state;
    scanf(" %s", str);
    for(len = 0; str[len]; len++){
        bucket[str[len]]++;
    }
    for(int i = 0; i < 10; i++){
        state = bucket[identifier[i]];
        if(!state)continue;
        for(int j = 0; base[order[i]][j]; j++){
            bucket[base[order[i]][j]] -= state;
        }
        for(int j = 0; j < state; j++)output[olen++] = order[i] + '0';
    }
    output[olen] = 0;
    std::sort(output, output + olen);
    printf("%s\n", output);
}

int main(){
    int T;
    scanf(" %d", &T);
    for(int i = 1; i <= T; i++){
        solve(i);
    }
}
