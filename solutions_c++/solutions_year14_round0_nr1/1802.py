#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int hash[20];

void solve(){
        int n;
        scanf("%d", &n);
        memset(hash, 0, sizeof(hash));
        for(int i=1;i<=4;++i){
                for(int j=0; j<4;++j){
                        int v;
                        scanf("%d", &v);
                        if(i==n)hash[v] = 1;
                }
        }
        scanf("%d", &n);
        int count = 0, ans = 0;
        for(int i=1;i<=4;++i){
                for(int j=0; j<4;++j){
                        int v;
                        scanf("%d", &v);
                        if(i==n){
                                if(hash[v] == 1){
                                        ++count;
                                        ans = v;
                                }
                        }
                }
        }
        if(count == 1)printf("%d\n", ans);
        else if(count == 0)printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
        return;
}

int main(){
        int T;
        scanf("%d", &T);
        for(int t=0;t<T;++t){
                printf("Case #%d: ", t+1);
                solve();
        }
}
