#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int vis[1100];
int cnt[1100];
int kk;

int check(int x)
{
    if(x<10) return 1;
    char tmp[5];
    itoa(x,tmp,10);
    int len=strlen(tmp);
    for(int i=0;i<len/2;i++)
        if(tmp[i]!=tmp[len-1-i]) return 0;
    return 1;
}

void init()
{
    for(int i=1;i<=100;i++){
        if(check(i)){
            int j=i*i;
            if(j<=1000&&check(j)) vis[j]=1;
        }
    }
    for(int i=1;i<=1000;i++)
        cnt[i] = cnt[i-1]+vis[i];
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int cas;
    kk=0;
    init();
    scanf("%d",&cas);
    while(cas--){
        int a,b;
        scanf("%d%d",&a,&b);
        printf("Case #%d: %d\n",++kk,cnt[b]-cnt[a-1]);
    }
    return 0;
}
