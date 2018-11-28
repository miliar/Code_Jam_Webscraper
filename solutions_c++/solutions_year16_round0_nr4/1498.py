#include <cstdio>

int K, C, S, cover, cnt;
long long ans[110];

void bkt(long long pos, int depth){
//    printf("pos = %lld, depth = %d\n", pos, depth);
    
    if(depth == C){
        if(cover < pos%K){
            cover = pos%K;
            ans[cnt++] = pos+1;
            S--;
        }
        
        return;
    }
    
    if(pos%K == K-1){
        bkt((pos+1)*K-1, depth+1);
        return;
    }
    
    long long p = pos*K + 1;
    
    while(p%K != 0 and cover < K-1 and S > 0){
        bkt(p, depth+1);
        p++;
    }
}

int main(){
    int T, tc = 0;
    scanf("%d", &T);
    
    while(T--){
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", ++tc);
        
        cover = -1; cnt = 0;
        for(int i=0; i<K and cover < K-1 and S > 0; i++) bkt(i, 1);
        
        if(cover == K-1){
            for(int i=0; i<cnt; i++){
                printf(" %lld", ans[i]);
            }
            
            printf("\n");
        } else {
            printf(" IMPOSSIBLE\n");
        }
    }
}
