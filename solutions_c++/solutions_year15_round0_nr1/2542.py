#include <cstdio>

int main(){
    int T;
    scanf("%d",&T);
    for(int c = 0 ; c < T ; c++){
        int A;
        char B[1010];
        scanf("%d %s",&A,B);
        int now = 0, sol = 0;
        for(int d = 0 ; d <= A ; d++){
            if(now < d){
                sol += d-now;
                now = d;
            }
            now += B[d]-'0';
        }
        printf("Case #%d: %d\n",c+1,sol);
    }
}
