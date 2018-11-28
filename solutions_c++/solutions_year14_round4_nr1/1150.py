#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;
int v[101010];
int pairx[101010];
int st,dr;
int N,K,T,ind;
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        ++ind;
        scanf("%d%d",&N,&K);
        for(int i=1;i<=N;++i){
            scanf("%d",&v[i]);
            pairx[i]=0;
        }
        sort(v+1,v+N+1);
        int st=1;int dr=N;
        while(st<dr){
            if(v[st]+v[dr] <= K){
                pairx[st]=1;
                ++st;--dr;
            }else {
                --dr;
            }
        }
        int ret = 0;
        for(int i=1;i<=N;++i){
            if(pairx[i]==0)
                ++ret;
        }
        printf("Case #%d: %d\n",ind,ret);
    }
}
