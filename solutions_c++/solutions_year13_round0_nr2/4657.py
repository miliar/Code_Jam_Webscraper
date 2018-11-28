#include<cstdio>
#include<cmath>
#include<iostream>
#include<ctime>
#include<cstring>
#include<algorithm>
#include<string>
#include<queue>
#define L(r) (r<<1)
#define R(th) (th<<1|1)
#define LL long long
using namespace std;
#define MA 12

 //priority_queue<int, vector<int>,greater<int> > q;
int map[105][105];
int heng[105];
int shu[105];
int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n,m;
    int cas;
    int cc=0;
    scanf("%d",&cas);
    while(cas--){
        memset(heng,0,sizeof(heng));
        memset(shu,0,sizeof(shu));
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;++i)
           for(int j=0;j<m;++j){
              scanf("%d",&map[i][j]);
              heng[i]=max(heng[i],map[i][j]);
              shu[j]=max(shu[j],map[i][j]);
           }
        int can=1;
        for(int i=0;i<n;++i){
           for(int j=0;j<m;++j)
              if(heng[i]>map[i][j] && shu[j]>map[i][j]){
                 can=0;
                 break;
              }
        }
        if(can)
        printf("Case #%d: YES\n",++cc);
        else
        printf("Case #%d: NO\n",++cc);
    }

    return 0;
}
/*
LL x,y;
LL exgcd(LL a,LL b,LL &x,LL &y){
    LL res,t;
    if(b==0)
    {
        x=1;y=0;
        return a;//·µ»ØµÄÊÇgcd£»
    }
    res=exgcd(b,a%b,x,y);
    t=x;
    x=y;
    y=t-(a/b)*y;
    return res;
}
LL fast_mod(__int64 js,__int64 cs,__int64 mod) {
    __int64 t=js%mod,res=1;
    while(cs) {
        if(cs&1)
           res=res*t%mod;
        t=t*t%mod;
        cs>>=1;
    }
    return res;

}
*/
