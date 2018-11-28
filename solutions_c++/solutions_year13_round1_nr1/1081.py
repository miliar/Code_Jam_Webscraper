#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        
        int r, x, i;
        scanf("%d%d",&r,&x);
        for(i=0;1;i++,r+=2){
            if((r+1)*(r+1)-r*r > x)
                break;
            x -= (r+1)*(r+1)-r*r;
        }
        
        printf("Case #%d: %d\n", tt, i);
    }
    return 0;
}

