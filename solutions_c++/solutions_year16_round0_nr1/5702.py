#include<bits/stdc++.h>
using namespace std;
bool u[10]={};
bool check(){
    for(int i=0;i<10;i++)
        if(u[i]==0)return 1;
    return 0;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,n,Case=0;
    scanf("%d",&T);
    while(T--){
        memset(u,0,sizeof(u));
        scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",++Case);
            continue;
        }
        long long N=0;
        do{
            N+=n;
            long long tmp=N;
            while(tmp){
                u[tmp%10]=1;
                tmp/=10;
            }
        }while(check());
        printf("Case #%d: %lld\n",++Case,N);
    }
    return 0;
}
