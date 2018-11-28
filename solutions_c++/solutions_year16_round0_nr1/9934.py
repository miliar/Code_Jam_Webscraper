#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <cmath>
#define LL long long
using namespace std;
int n,cnt;
int vis[15];
void get(LL x){
    int a=0,b=x;
    while(b){
        a=b%10;
        if(vis[a]==0){vis[a]=1;cnt++;}
        b/=10;
    }
}
int main()
{
    freopen("ldata.in","r",stdin);
    freopen("ldata.out","w",stdout);

    int id=0;

    int t;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        if(n==0) {printf("Case #%d: INSOMNIA\n",++id);continue;}
        cnt=0;
        memset(vis,0,sizeof(vis));
        LL m=0;
        while(cnt<10){
            m+=n;
            get(m);
            //cout<<'a'<<m<<endl;
        }
        printf("Case #%d: %d\n",++id,m);
    }
    return 0;
}
