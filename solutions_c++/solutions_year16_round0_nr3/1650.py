#include <cstdio>

const int PRM = 10000;

int jamcoin[500];
int divisor[500][11];
int pos = 0;

int rem[PRM][11][32];

bool check(int n, int base){
    for(int i=2;i<=PRM;i++){
        int r = 0;
        for(int j=0;j<32;j++){
            if((n>>j) & 1){
                r += rem[i][base][j];
                r %= i;
            }
        }
        if(r == 0){
            jamcoin[pos] = n;
            divisor[pos][base] = i;
            return true;
        }
    }
    return false;
}

int main(){
    for(int i=2;i<=PRM;i++){
        for(int j=2;j<=10;j++){
            rem[i][j][0] = 1;
            for(int k=1;k<32;k++){
                rem[i][j][k] = (rem[i][j][k-1] * j) % i;
            }
        }
    }
    int T; scanf("%d", &T);
    for(int ti=1;ti<=T;ti++){
        printf("Case #%d:\n", ti);
        int n, m; scanf("%d%d", &n, &m);
        for(int k=0;k<(1<<(n-2));k++){
            bool det = true;
            int t = (1 << (n-1)) | (k<<1) | 1;
            for(int base=2;base<=10;base++){
                if(!check(t, base)){
                    det = false;
                    break;
                }
            }
            if(det){
                pos++;
                if(pos == m) break;
            }
        }
        for(int i=0;i<m;i++){
            for(int j=n-1;j>=0;j--){
                printf("%d", (jamcoin[i]>>j)&1);
            }
            for(int j=2;j<=10;j++){
                printf(" %d", divisor[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
