#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int abs(int a){
    return a>0?a:-a;
}

int main(){
    int k,c,s,T,icas=0;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d",&k,&c,&s);
        if(s<k){
            printf("Case #%d: IMPOSSIBLE\n",++icas);
        }
        printf("Case #%d: ",++icas);
        for(int i=1;i<s;i++){
            printf("%d ",i);
        }
        printf("%d\n",s);
    }
    return 0;
}
