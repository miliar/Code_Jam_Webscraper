#include <iostream>
#include <vector>
#include <math.h>
#include <cmath>

using namespace std;

int main(){
    int tc,k,c,s;
    scanf("%d",&tc);
    for(int tci=1;tci<=tc;tci++){
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d: %d",tci,1);
        for(int i=2;i<=k;i++){
            printf(" %d",i);
        }
        printf("\n");
    }
    return 0;
}