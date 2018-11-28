#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int A[2005],B[2005];
int TA[2005],TB[2005];
int Ans[2005],Hash[2005];
void Redo(int n){
    int i,j;
    for(i=1;i<=n;i++)if(Hash[i]){
        TA[i]=1;
        for(j=1;j<i;j++)
            if(Hash[j]&&Ans[j]<Ans[i])TA[i]=max(TA[i],TA[j]+1);
    }
    for(i=n;i>=1;i--)if(Hash[i]){
        TB[i]=1;
        for(j=i+1;j<=n;j++)
            if(Hash[j]&&Ans[j]<Ans[i])TB[i]=max(TB[i],TB[j]+1);
    }
}
int n,fl;
void dfs(int p){
    if(p>n){
        fl=1;
        return ;
    }
    int i,j;
    for(i=1;i<=n;i++)if(!Hash[i]){
        Ans[i]=p;
        Hash[i]=1;
        Redo(n);
        for(j=1;j<=n;j++)
            if(Hash[j]&&(TA[j]!=A[j]||TB[j]!=B[j]))break;
        if(j>n)dfs(p+1);
        if(fl)return ;
        Hash[i]=0;
    }
    return ;
}
int main(){
    int i,j,k,l,T,tt=0;
freopen("C.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        tt++;
        scanf("%d",&n);
        memset(Hash,0,sizeof(Hash));
        memset(TA,0,sizeof(TA));
        memset(TB,0,sizeof(TB));
        for(i=1;i<=n;i++)scanf("%d",&A[i]);
        for(i=1;i<=n;i++)scanf("%d",&B[i]);
        for(i=1;i<=n;i++)
            if(A[i]==1&&B[i]==1)break;
        Hash[i]=1;
        Ans[i]=1;
        Redo(n);
        fl=0;
        dfs(2);
        printf("Case #%d:",tt);
        for(i=1;i<=n;i++)printf(" %d",Ans[i]);
        putchar('\n');
    }
    return 0;
}
