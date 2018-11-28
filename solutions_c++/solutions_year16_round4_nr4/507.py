#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
const int N=202;
int n,k;
int gun(int x){
    int cnt=0;
    while(x){
        if(x&1)cnt++;
        x/=2;
    }
    return cnt;
}
int aa[N],bb[N];
char ss[N][N];

int fun(int id){
    for(int i=0;i<n;i++)aa[i]=i;
    do{
        for(int i=0;i<n;i++)bb[i]=i;
        do{
            for(int i=0;i<n;i++){
                int flag=0;
                for(int j=i;j<n;j++){
                    if(id&(1<<(aa[i]*n+bb[j])))flag=1;
                }
                if(!flag)return 0;
                if(id&(1<<(aa[i]*n+bb[i])))continue;
                else break;
            }
        }while(next_permutation(bb,bb+n));
    }while(next_permutation(aa,aa+n));
    return 1;
}
int main(){
    #ifdef DouBi
    freopen("in.cpp","r",stdin);
    freopen("out.cpp","w",stdout);
    #endif // DouBi
    int T;scanf("%d",&T);
    int cas=1;
    while(T--){
        printf("Case #%d: ",cas++);
        scanf("%d",&n);
        for(int i=0;i<n;i++)scanf("%s",ss[i]);
        int xx=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(ss[i][j]=='1')xx|=1<<(i*n+j);
            }
        }
        int x=n*n;
        int ans=x;
        for(int i=0;i<(1<<x);i++)if((xx&i)==xx){
            if(fun(i)){
                ans=min(ans,gun(i^xx));
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
