#include<cstdio>

int z,n,m, x;
int t[10];

int main(){
    t[0] = 1;
    t[1] = 4;
    t[2] = 9;
    t[3] = 121;
    t[4] = 484;
    scanf("%d", &z);
    int k = 0;
    while(z--){
        
    x = 0;
        k++;
        scanf("%d %d", &n,&m);
        for(int i = 0; i < 5; ++i){
            if((t[i] >= n) &&  (t[i] <= m)){
                x++;
            }
        }
        printf("Case #%d: %d\n", k, x);
    }
}
