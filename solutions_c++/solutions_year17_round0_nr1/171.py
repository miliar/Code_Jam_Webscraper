#include <bits/stdc++.h>

using namespace std;

int main(void){
    freopen("testin.txt","r",stdin);
    freopen("testout.txt", "w", stdout);
    int tt;
    char pancake[1005];
    int s,k;
    cin >> tt;
    
    for(int t=1; t<=tt; t++){
        cin >> pancake;
        cin >> k;
        s = strlen(pancake);
        //printf("string is %s k is %d length is %d\n", pancake, k, strlen(pancake));
        int pc[1005];
        for(int i=0;i<s;i++){
            if(pancake[i]=='+') pc[i] = 1;
            else pc[i] = 0;
        }
        int moves=0;
        for(int i=0;i<s-k+1;i++){
            if(pc[i]==0){
                for(int j=i;j<i+k;j++){
                    pc[j]=1-pc[j];
                }
                moves++;
            }
        }
        int done=1;
        for(int i=s-k+1;i<s;i++){
            if(pc[i]==0){
                done=0;
                break;
            }
        }
        
        printf("Case #%d: ", t);
        if(done){
            printf("%d\n", moves);
        }else{
            printf("IMPOSSIBLE\n");
        }
    }
    
    return 0;
}
