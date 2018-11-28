#include<bits/stdc++.h>
using namespace std;
int ar[655360],bit[17],prime[6]={2,3,5,7,11,13},ans[10];
int func(int x){
    int ct=0;
    while(x){
        bit[ct++]=x%2;
        x/=2;
    }
    return 0;
}
int func2(int x){
    long long num=0,pow=1;
    for(int i=0;i<=15;++i){
        num=num+bit[i]*pow;
        pow*=x;
    }
    for(int i=0;i<6;++i){
        if(num%prime[i]==0){
            ans[x]=prime[i];
            return 1;
        }
    }
    return 0;
}
int main(){
    int T=1;
    freopen("y.txt","w",stdout);
    printf("Case #1:\n");
    for(int t=1;t<=T;++t){
        int N=16,J=50,cnt=0;
        for(int i=(1<<15)+1;i<1<<16 && cnt<50;i+=2){
            memset(bit,0,sizeof(bit));
            func(i);
            int ct=0;
            for(int j=2;j<=10;++j){
                ct+=func2(j);
            }
            if(ct==9){
                ++cnt;
                for(int j=15;j>=0;--j){
                    printf("%d",bit[j]);
                }
                for(int j=2;j<=10;++j)
                    printf(" %d",ans[j]);
                printf("\n");
            }
        }
        //printf("%d\n",cnt);
    }
    return 0;
}
