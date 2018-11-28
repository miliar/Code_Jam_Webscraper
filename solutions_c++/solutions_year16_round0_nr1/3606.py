#include <iostream>
#include <vector>
#include <math.h>
#include <cmath>

using namespace std;

int LIMIT = (1<<10)-1;

int main(){
    int tc,n;
    scanf("%d",&tc);
    for(int tci=1;tci<=tc;tci++){
        scanf("%d",&n);
        if(n==0) {printf("Case #%d: INSOMNIA\n",tci);continue;}
        int mask=0,mul=1;
        long long curn;
        while(mask < LIMIT){
            curn = n*mul++;
            while(curn>0){
                mask |= (1<<curn%10);
                curn /= 10;
            }
        }
        printf("Case #%d: %lld\n",tci,n*(mul-1));
    }
    return 0;
}