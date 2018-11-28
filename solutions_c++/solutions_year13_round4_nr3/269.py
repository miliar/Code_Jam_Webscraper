#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define MS0(A) memset(A,0,sizeof(A));
#define rep(i,n) for(int i=0;i<n;i++)
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define red(i,n) for(int i=n-1;i>=0;i--)
#define DA(A,n) {cout<<#A;rep(iii,n)cout<<' '<<A[iii];cout<<endl;}
#define D(x) {cout<<#x<<' '<<(x)<<endl;}
#define DD(x,y) {cout<<#x<<' '<<x<<' ';cout<<#y<<' '<<y<<endl;}
#define DDD(x,y,z) {cout<<#x<<' '<<x<<' ';cout<<#y<<' '<<y<<' ';cout<<#z<<' '<<z<<endl;}
#define read2(x,y) {read(x);read(y);}
#define read3(x,y,z) {read(x);read(y);read(z);}
using namespace std;
typedef long long LL;
const int MAXN=111111;
const int oo=0X1FFFFFFF;
int PP=1000000007;
const long double PI=3.141592653589793;
template<typename TT>
void read(TT &x)
{
    char ch;
	for (ch=getchar(); ch>'9'||ch<'0'; ch=getchar()) ;
	for (x=0; ch>='0'&&ch<='9'; ch=getchar()) x=x*10+ch-48;
}
struct edge{
	int v;
	edge *n;
} *hd[MAXN],Epool[MAXN+MAXN];
int ent;
void addedge(int u,int v){
    //DD(u,v)
	edge *p=&Epool[ent++];
	p->n=hd[u];p->v=v;hd[u]=p;
}
int n,a[2222],dis[2222],Q[22222],v[2222],l,r;
int V[2222];
void dfs(int u){
	V[u]=1;
	dis[u]++;
    for(edge *p=hd[u];p!=NULL;p=p->n){
        int y=p->v;
        if(!V[y]&&dis[u]==dis[y])dfs(y);
    }
}

void Init(){
    read(n);
    rep(i,n)hd[i]=NULL;ent=0;
    rep(i,n){
        read(a[i]);
        addedge(n,i);
        for(int j=i;j--;)
            if(a[j]==a[i]){addedge(i,j);break;}
        for(int j=i;j--;)
            if(a[j]==a[i]-1){addedge(j,i);break;}
    }
    rep(i,n) read(a[i]);
    rep(i,n){
        for(int j=i+1;j<n;j++)
            if(a[j]==a[i]){addedge(i,j);break;}
        for(int j=i+1;j<n;j++)
            if(a[j]==a[i]-1){addedge(j,i);break;}
    }
    rep(i,n)dis[i]=0;
    Q[l=0]=n;r=1;
    v[n]=1;
    for(;l<r;){
        int x=Q[l];l++;
        for(edge *p=hd[x];p!=NULL;p=p->n){
            int y=p->v;
            	if(dis[y]<dis[x]+1){
				dis[y]=dis[x]+1;
				if(!v[y]){
					v[y]=1;
					Q[r++]=y;
				}
			}
        }v[x]=0;
    }
    rep(i,n)if(i){
        bool ok=0;
        rep(j,n){
            if(dis[j]==i){
                if(ok) dfs(j); else ok=1;
            }
        }
    }
    rep(i,n)printf(" %d",dis[i]);
    printf("\n");
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;read(T);
    rep(i,T){
        cout<<"Case #"<<i+1<<":";
        Init();
    }
}
