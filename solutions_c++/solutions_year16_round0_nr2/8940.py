#include <bits/stdc++.h>


uint32_t fetchance(char* str){
    uint32_t len = strlen(str);
    uint32_t i;
    uint32_t tns = 0;
    for(i=0; i<(len-1); i++){
        tns += str[i] != str[i+1];
    }
    if(str[len-1] == '-'){
        tns++;
    }
    return tns;
}

int main(int argc, char** argv){
    freopen("k.in", "r", stdin);
freopen("b.out", "w+", stdout);
    uint32_t tc = 0;
    uint32_t i = 0;
    scanf("%d", &tc);
    for(i=0; i<tc; i++){
        char str[101];
        scanf("%s", &str);
        printf("Case #%d: %d\n", i+1, fetchance(str));
    }
    return 0;
}
