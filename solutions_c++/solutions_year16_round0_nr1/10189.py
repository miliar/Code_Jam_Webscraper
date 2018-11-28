#include <bits/stdtr1c++.h>
#define read() freopen("A-large.in", "r", stdin)
#define write() freopen("A-large.out", "w", stdout)
using namespace std;

int main(){
    read();
    write();
    int N, r, T, mul, asleep=0, countd, i,n;
    scanf("%d",&T);
    for(int x=1; x<=T; x++){
        int digit[]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
        scanf("%d",&N);
        if(N==0){
            printf("Case #%d: INSOMNIA\n", x);
        }
        else if(N>0){
            countd=0;
            i=1;
            while(1){
                    mul = N * i;
                    n = mul;
                    while(n){
                        r = n%10;
                        n = n / 10;
                        if(digit[r]==-1){
                            digit[r]=r;
                            countd++;
                        }
                    }
                   if(countd == 10){
                        asleep = mul;
                        break;
                    }
                    i++;
            }
            printf("Case #%d: %d\n", x, asleep);
        }
    }
    return 0;
}
