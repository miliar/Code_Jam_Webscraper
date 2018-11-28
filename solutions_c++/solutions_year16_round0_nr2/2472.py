#include <cstdio>
#include <string>
#include <iostream>
#include <cstring>
using namespace std;
#define MAXN 110
char input[MAXN], len;
int process(){
    //토큰화
    int token_num = 0;
    char now_sign = input[0];
    for(int i = 1 ; i < len; i++){
        if(now_sign != input[i]){
            now_sign = input[i];
            token_num++;
        }
    }
    return token_num + (now_sign == '-');
}
int main(){
    int T;
    FILE * ifp = fopen("/Users/clsrn1581/Desktop/codejam/B/B-large.in", "r");
    FILE * ofp = fopen("/Users/clsrn1581/Desktop/codejam/B/B-large.out", "w");
    
    fscanf(ifp, "%d", &T);
    for(int t = 1 ; t <= T; t++){
        fscanf(ifp, "%s\n", input);
        len = strlen(input);
         fprintf(ofp , "Case #%d: %d\n", t, process());
    }
}