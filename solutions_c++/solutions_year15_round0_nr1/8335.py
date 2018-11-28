#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main() {
    int T;
    scanf("%d",&T);
    for (int i=1; i<=T; i++) {
        int S_max, need=0;
        char S [2001];
        scanf("%d %2000s",&S_max,&S);
        int cur=S[0]-'0';
        for (int j=1; j<=S_max; j++) {
            while (cur<j) {
                cur++; need++;
            }
            cur+=S[j]-'0';
        }
        printf("Case #%d: %d \n",i,need);
    }
    return 0;
}
