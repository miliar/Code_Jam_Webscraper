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
#define MA 50005
struct EG{
  int u,v;
  int next;
  double len;
}eg[1000];
struct Node{
   int type;
   int sec;
}node[40];
int head[100];
int tot=0;
int n,m;
int nm,nt,ns,nr;
int S;
double dp[50][8][8][8][8][6];
void init(){
   memset(head,-1,sizeof(head));
   tot=0;
   for(int i=0;i<=30;++i)
      node[i].type=0;
   for(int i=0;i<=n;++i)
     for(int j=0;j<(1<<nm);++j)
        for(int k=0;k<(1<<nt);++k)
           for(int d=0;d<(1<<ns);++d)
              for(int e=0;e<(1<<nr);++e)
                for(int v=0;v<=(ns+nr);++v)
                   dp[i][j][k][d][e][v]=1e40;
}
void addeg(int u,int v,double len){
     eg[tot].u=u;
     eg[tot].v=v;
     eg[tot].len=len;
     eg[tot].next=head[u];
     head[u]=tot++;

     eg[tot].u=v;
     eg[tot].v=u;
     eg[tot].len=len;
     eg[tot].next=head[v];
     head[v]=tot++;
}
struct BC{
   int n;
   int n1,n2,n3,n4,v;
}use,bf,nx;
queue<BC> qq;
int in[40][8][8][8][8][6];
double vv[6]={30,35,40,45,50,55};
void getans(){
     while(!qq.empty()){
        qq.pop();
     }
     use.n=0;
     use.n1=0;
     use.n2=0;
     use.n3=0;
     use.n4=0;
     use.v=0;
     qq.push(use);
     memset(in,0,sizeof(in));
     int n0,n1,n2,n3,n4,v,u;
     while(!qq.empty()){
          bf=qq.front();
          qq.pop();
          u=n0=bf.n;
          n1=bf.n1;
          n2=bf.n2;
          n3=bf.n3;
          n4=bf.n4;
          v=bf.v;
          in[n0][n1][n2][n3][n4][v]=0;

          for(int i=head[n0];i!=-1;i=eg[i].next){
              //int u=eg[i].u;
              int V=eg[i].v;
              double lenn=eg[i].len;
              double tt=lenn/vv[v];
                if(node[V].type==0){
                   if(dp[V][n1][n2][n3][n4][v]>dp[u][n1][n2][n3][n4][v]+tt){
                     dp[V][n1][n2][n3][n4][v]=dp[u][n1][n2][n3][n4][v]+tt;
                     if(!in[V][n1][n2][n3][n4][v]){
                        in[V][n1][n2][n3][n4][v]=1;
                        nx.n=v;
                        nx.n1=n1;
                        nx.n2=n2;
                        nx.n3=n3;
                        nx.n4=n4;
                        nx.v=v;
                        qq.push(nx);
                     }
                   }
                 }
                 else if(node[V].type==1){
                     if(dp[V][n1|(1<<node[V].sec)][n2][n3][n4][v]>dp[u][n1][n2][n3][n4][v]+tt){
                         dp[V][n1|(1<<node[V].sec)][n2][n3][n4][v]=dp[u][n1][n2][n3][n4][v]+tt;
                         if(!in[V][n1|(1<<node[V].sec)][n2][n3][n4][v]){
                          in[V][n1|(1<<node[V].sec)][n2][n3][n4][v]=1;
                          nx.n=v;
                          nx.n1=n1|(1<<node[V].sec);
                          nx.n2=n2;
                          nx.n3=n3;
                          nx.n4=n4;
                          nx.v=v;
                          qq.push(nx);
                         }
                     }
                 }
                 else if(node[v].type==2){
                     if(dp[V][n1][n2|(1<<node[V].sec)][n3][n4][v]>dp[u][n1][n2][n3][n4][v]+tt){
                         dp[V][n1][n2|(1<<node[V].sec)][n3][n4][v]=dp[u][n1][n2][n3][n4][v]+tt;
                         if(!in[V][n1][n2|(1<<node[V].sec)][n3][n4][v]){
                          in[V][n1][n2|(1<<node[V].sec)][n3][n4][v]=1;
                          nx.n=v;
                          nx.n1=n1;
                          nx.n2=n2|(1<<node[V].sec);
                          nx.n3=n3;
                          nx.n4=n4;
                          nx.v=v;
                          qq.push(nx);
                         }
                     }
                 }
                 else if(node[v].type==3){
                     if(dp[V][n1][n2][n3|(1<<node[V].sec)][n4][v+1]>dp[u][n1][n2][n3][n4][v]+tt){
                         dp[V][n1][n2][n3|(1<<node[V].sec)][n4][v+1]=dp[u][n1][n2][n3][n4][v]+tt;
                         if(!in[V][n1][n2][n3|(1<<node[V].sec)][n4][v+1]){
                          in[V][n1][n2][n3|(1<<node[V].sec)][n4][v+1]=1;
                          nx.n=v;
                          nx.n1=n1;
                          nx.n2=n2;
                          nx.n3=n3|(1<<node[V].sec);
                          nx.n4=n4;
                          nx.v=v+1;
                          qq.push(nx);
                         }
                     }
                 }
                 else{
                     if(dp[V][n1][n2][n3][n4][v]>dp[u][n1][n2][n3][n4][v]+tt){
                       dp[V][n1][n2][n3][n4][v]=dp[u][n1][n2][n3][n4][v]+tt;
                       if(!in[V][n1][n2][n3][n4][v]){
                        in[V][n1][n2][n3][n4][v]=1;
                        nx.n=v;
                        nx.n1=n1;
                        nx.n2=n2;
                        nx.n3=n3;
                        nx.n4=n4;
                        nx.v=v;
                        qq.push(nx);
                      }
                     }
                     if(dp[V][n1][n2][n3][n4|(1<<node[V].sec)][v+1]>dp[u][n1][n2][n3][n4][v]+tt+3){
                         dp[V][n1][n2][n3][n4|(1<<node[V].sec)][v+1]=dp[u][n1][n2][n3][n4][v]+tt+3;
                         if(!in[V][n1][n2][n3][n4|(1<<node[V].sec)][v+1]){
                          in[V][n1][n2][n3][n4|(1<<node[V].sec)][v+1]=1;
                          nx.n=v;
                          nx.n1=n1;
                          nx.n2=n2;
                          nx.n3=n3;
                          nx.n4=n4|(1<<node[V].sec);
                          nx.v=v+1;
                          qq.push(nx);
                         }
                     }


                 }

          }

     }


}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   int N,R,T,l,r;
   int cas;
   int cc=0;
   scanf("%d",&cas);
   while(cas--){
        scanf("%d%d",&R,&T);
        l=0;r=1000;
        while(l<=r){
          int mid=(l+r)>>1;
          if((2*R+2*mid-1)*mid<=T)
              l=mid+1;
          else
                r=mid-1;
        }

        printf("Case #%d: %d\n",++cc,r);
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
