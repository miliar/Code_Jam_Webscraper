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
#include<ext/rope>
#define __rope __gnu_cxx::
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
template<typename TT> void read2(TT &x,TT &y){read(x);read(y);}
template<typename TT> void read3(TT &x,TT &y,TT &z){read(x);read(y);read(z);}

int n,m,a[111][111],f[111],g[111];
void Init(){
    read2(n,m);
    rep(i,n)rep(j,m)read(a[i][j]);
    MS0(f);MS0(g);
    rep(i,n)rep(j,m)f[i]=max(f[i],a[i][j]);
    rep(i,n)rep(j,m)g[j]=max(g[j],a[i][j]);
    bool yes=1;
    rep(i,n)rep(j,m)
    if(a[i][j]!=min(f[i],g[j])) {yes=0;break;}
    puts(yes?"YES":"NO");
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;read(T);
    rep(i,T){
        cout<<"Case #"<<(i+1)<<": ";
        Init();
    }
}
