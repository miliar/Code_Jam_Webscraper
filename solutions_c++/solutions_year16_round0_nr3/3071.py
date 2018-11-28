#include<cstdio>
#include<cctype>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<complex>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<utility>
#include<list>
#include<bitset>
using namespace std;

#define LL long long
#define LL_ __int64
#define rep(i,j,k) for(int i=(j);i<=(k);i++)
#define repp(i,j,k) for(int i=(j);i>=(k);i--)
#define Add(u,v,w) {E[++tot]=(Edge){u,v,w,Last[u]}; Last[u]=tot;}
#define mst(i,j) memset(i,j,sizeof(i))
#define scf(i) scanf("%d",&(i))
#define scff(i,j) scanf("%d%d",&(i),&(j))
#define scfs(i) scanf("%s",(i))
#define pii pair<int,int>
#define vec vector
#define mp make_pair
#define bt bitset
#define pq priority_queue
#define bgn begin
#define ist insert
#define fnd find
#define cnt count
#define rmv remove
#define psb push_back
#define lbd lower_bound
#define ubd upper_bound
#define bsc binary_search
#define fst first
#define scd second
#define psh push
#define frt front
#define ers erase
#define rvs reverse
#define it iterator

#define MOD 1000000007
#define maxn 500010
#define maxm 300010
#define pi acos(-1.0)
#define INF 0x7fffffff
#define eps 1e-5
#define IN freopen("In.txt","r",stdin)
#define OUT freopen("Out.txt","w",stdout)
#define CMP system("comp In.txt Out.txt")

LL gcd(LL a,LL b){
    return a==0? b:gcd(b%a,a);
}

LL qmulti(LL a,LL i,LL n){
    LL res=0;
    while(i){
        if(i&1) res=(res+a)%n;
        i>>=1; a=(a+a)%n;
    }
    return res;
}

LL qmod(LL a,LL i,LL n){
    LL res=1;
    while(i){
        if(i&1) res=qmulti(res,a,n);
        i>>=1; a=qmulti(a,a,n);
    }
    return res;
}

bool check(LL n,LL a,LL d){
    if(n==2 || n==a) return true;
    if((n&1)==0)  return false;
    while((d&1)==0) d>>=1;
    LL t=qmod(a,d,n);
    while( (d!=n-1) && (t!=1) && (t!=n-1) ){
        t=qmulti(t,t,n); d<<=1;
    }
    return ( t==n-1 || (d&1)==1 );
}

bool Miller(LL n){			//ËØÊý²âÊÔ
    if(n<2) return false;
    int a[]={2,3,61};
    for(int i=0;i<3;i++) if(!check(n,a[i],n-1))
        return false;
    return true;
}

LL Pollard_rho(LL x,LL c){
    LL i=1,k=2;
    srand(time(NULL));
    LL x0=rand()%(x-1)+1;
    LL y=x0;
    while(1){
        i++;
        x0=(qmulti(x0,x0,x)+c)%x;
        LL d=gcd(y-x0,x); if(d<0) d=-d;
        if(d!=1 && d!=x) return d;
        if(y==x0) return x;
        if(i==k) { y=x0; k+=k; }
    }
}

LL Pow(LL a,LL b){
    LL ans=1;
    while(b--) ans*=a;
    return ans;
}

bool Judge(int n,int b){
    bt<30> v=n;
    LL ans=0;
    rep(i,0,15) ans+=Pow(b,i)*v[i];
    //cout<<v<<" "<<b<<" "<<ans<<endl;
    if(Miller(ans)) return true;
    return false;
}

int main(){OUT;
    int T; scf(T); scf(T); scf(T);
    int s=(1<<15)+1;
    int cnt=0;
    vec<int> v;
    while(cnt<50){
        int tot=0;
        rep(i,2,10) if(!Judge(s,i)) tot++;
            else break;
        if(tot==9) { cnt++; v.psb(s); }
        s+=2;
    }
    puts("Case #1:");
    rep(i,0,49){
        bt<16> x=v[i];
        cout<<x;
        rep(j,2,10){
            LL ans=0;
            rep(k,0,15) ans+=Pow(j,k)*x[k];
            LL t=Pollard_rho(ans,110);
            printf(" %lld",t);
        }
        puts("");
    }
    return 0;
}
