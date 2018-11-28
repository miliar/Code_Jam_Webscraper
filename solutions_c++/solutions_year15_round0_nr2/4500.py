#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;
int T;
int solve(int x,int maxn){
    return x/maxn - (x%maxn==0?1:0);

}
int main (){
    scanf("%d",&T);
    for(int t =1 ; t <=T ;t++){
        int d;
        scanf("%d",&d);
        int p[1001];
        for(int i = 0 ; i < d ;i++)scanf("%d",&p[i]);
        int ans=2147483647;
        for(int i = *max_element(p,p+d);i>0;i--){
            int total=i;
            for(int j = 0; j< d ;j++){
                total+=solve(p[j],i);
            }
            if(ans!=min(total,ans)){
                ans=min(total,ans);
            }

        }
        printf("Case #%d: %d\n",t,ans);
    }

}
