#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int vis[10];
int cnt;

void init(){
    memset(vis,0,sizeof(vis));
    cnt=0;
}

bool check(int x){
    while(x){
        int t=x%10;
        if(!vis[t]){
            vis[t]=1;
            cnt++;
            if(cnt==10) break;
        }
        x/=10;
    }
    if(cnt==10) return true;
    return false;
}

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T,ca=0;
    int n,i;
    scanf("%d",&T);
    while(T--){
        ca++;
        init();
        scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",ca);
            continue;
        }
        int x=n;
        while(!check(x)){
            x+=n;
        }
        printf("Case #%d: %d\n",ca,x);
    }
    return 0;
}
