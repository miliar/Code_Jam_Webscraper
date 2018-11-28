#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;
typedef long long ll;
const int MAXN = 1e2+5;
char S[MAXN];

int main(){
    int N,T;
    scanf("%d",&T);
    for(int _i = 1 ; _i <= T ; _i++){
        scanf("%s",&S);
        int res = 0;
        int len = strlen(S);
        int end = len - 1;
        while(S[end] == '+') end--;
        for(int i = 0 ; i <= end ; i++){
            if( (i+1) <= end && S[i] == S[i+1])continue;
            else
                res++;          
        }
        
        printf("Case #%d: %d\n",_i,res);
    }
    return 0;
}