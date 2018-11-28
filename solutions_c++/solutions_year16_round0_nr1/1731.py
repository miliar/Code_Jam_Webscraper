#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("yLarge1.txt","w",stdout);
    int ar[10];
    int T,N;
    scanf("%d",&T);
    for(int i=1;i<=T;++i){
        scanf("%d",&N);
        memset(ar,0,sizeof(ar));
        if(N==0){
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        int cnt=0,ct=0;
        while(cnt!=10){
            ++ct;
            long long x=(long long)ct*N;
            while(x){
                if(ar[x%10]==0)
                    ++cnt;
                ar[x%10]=1;
                x/=10;
            }
        }
        printf("Case #%d: %lld\n",i,(long long)ct*N);
    }
    return 0;
}
