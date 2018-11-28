#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int T;
int now,n,c[11],cnt;
void add(int x){
    for (;x;x/=10){
        if (c[x%10]==0) cnt++;
        c[x%10]++;
    }
    return;
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
        printf("Case #%d: ",cas);
        //n=cas;
       scanf("%d",&n);
        now=n;cnt=0;
        if (n==0){
            printf("INSOMNIA\n");
            continue;
        }
        memset(c,0,sizeof(c));
        for (;cnt<10;now+=n){
            add(now);
        }
        printf("%d\n",now-n);
    }
    return 0;
}
