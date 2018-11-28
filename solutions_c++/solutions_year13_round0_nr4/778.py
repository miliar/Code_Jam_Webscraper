#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int kasus,dapat[40][40],ada[205],perlu[205],peti,kunci[205],dp[1<<20];
bool sudah[1<<20];

int proses(int bitmask) {
    if (bitmask == (1<<peti)-1) return -1;
    if (sudah[bitmask]) return dp[bitmask];
    sudah[bitmask] = true;
    
    dp[bitmask] = peti+1;
    for (int i=0;i<peti && dp[bitmask]==peti+1;++i) {
        if (bitmask & (1<<i)) continue;
        if (kunci[perlu[i]] == 0) continue;
        --kunci[perlu[i]];
        for (int j=0;j<ada[i];++j) ++kunci[dapat[i][j]];
        int sem = proses(bitmask | (1<<i));
        if (sem < peti+1) dp[bitmask] = i;
        else {
            ++kunci[perlu[i]];
            for (int j=0;j<ada[i];++j) --kunci[dapat[i][j]];
        }
    }
    
    return dp[bitmask];
}

int main() {
    scanf("%d",&kasus);
    for (int l=1,sem;l<=kasus;++l) {
        scanf("%d %d",&sem,&peti);
        memset(kunci,0,sizeof(kunci));
        for (int i=0,j;i<sem;++i) {
            scanf("%d",&j);
            ++kunci[j];
        }
        
        for (int i=0;i<peti;++i) {
            scanf("%d %d",&perlu[i],&ada[i]);
            for (int j=0;j<ada[i];++j) scanf("%d",&dapat[i][j]);
        }
        
        memset(sudah,0,sizeof(sudah));
        int jawab = proses(0);
        printf("Case #%d:",l);
        if (jawab == peti+1) printf(" IMPOSSIBLE\n");
        else {
            printf(" %d",jawab+1);
            int indeks = 0;
            for (int i=1;i<peti;++i) {
                indeks |= (1<<jawab);
                jawab = dp[indeks];            
                printf(" %d",jawab+1);
            }
            printf("\n");
        }
    }
    return 0;
}
