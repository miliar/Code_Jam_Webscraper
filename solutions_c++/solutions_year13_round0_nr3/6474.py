#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main(){
    int casen;
    int a,b;
    int caser = 1;
    int count;
    scanf("%d\n",&casen);
    int i;
    int sqpalin[5] = {1,4,9,121,484};
    while(casen--){
        scanf("%d %d\n",&a,&b);
        count = 0;
        for(i=0;i<5;++i){
            if(sqpalin[i] >= a && sqpalin[i] <= b)
                count++;
        }
        printf("Case #%d: %d\n",caser,count);
        caser++;
    }
    return 0;
}

