#include <cstdio>
int main(){
    int T; scanf("%d", &T);
    for(int ti=1;ti<=T;ti++){
        printf("Case #%d:", ti);
        int k, c, s; scanf("%d%d%d", &k, &c, &s);
        if(k == 1){
            printf(" 1\n");
            continue;
        }
        else if(c == 1){
            if(k == s){
                for(int i=1;i<=k;i++) printf(" %d", i);
                printf("\n");
                continue;
            }
            else{
                printf(" IMPOSSIBLE\n");
                continue;
            }
        }
        else{
            if(s >= k-1){
                long long offset = k;
                for(int i=0;i<c-2;i++) offset *= k;
                long long pos = 1;
                for(int i=0;i<k-1;i++){
                    pos += offset;
                    printf(" %lld", pos);
                }
                printf("\n");
                continue;
            }
            else{
                printf(" IMPOSSIBLE\n");
                continue;
            }
        }
    }
    return 0;
}
