#include<bits/stdc++.h>
using namespace std;
int T,n;
int use[1001];
int main(){
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    scanf("%d",&T);
    for(int ti=1;ti<=T;ti++){
        scanf("%d",&n);
        printf("Case #%d: ",ti);
        if(n==0){
            printf("INSOMNIA\n");
            continue;
        }
        for(int i=0;i<10;i++) use[i]=0;
        for(int i=1;i<10000;i++){
            int x=n*i;
            while(x){
                use[x%10]=1;
                x/=10;
            }
            int ok=1;
            for(int j=0;j<10;j++)if(!use[j]){
                ok=0;
            }
            if(ok){
                printf("%d\n",n*i);
                break;
            }
        }
    }
}
