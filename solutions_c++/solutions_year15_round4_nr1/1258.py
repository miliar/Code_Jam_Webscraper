#include    <bits/stdc++.h>
#define     SF              scanf
#define     PF              printf
#define     END             feof(stdin)
#define     GL(a)           getline(cin,a)
#define     S1(a)           SF("%d",&a);
#define     S2(a,b)         SF("%d%d",&a,&b);
#define     S3(a,b,c)       SF("%d%d%d",&a,&b,&c);
#define     S4(a,b,c,d)     SF("%d%d%d%d",&a,&b,&c,&d);
#define     S5(a,b,c,d,e)   SF("%d%d%d%d%d",&a,&b,&c,&d,&e);
#define     P1(a)           PF("%d ",a);
#define     P2(a,b)         PF("%d %d ",a,b);
#define     P3(a,b,c)       PF("%d %d %d ",a,b,c);
#define     P4(a,b,c,d)     PF("%d %d %d %d ",a,b,c,d);
#define     P5(a,b,c,d,e)   PF("%d %d %d %d %d ",a,b,c,d,e);
#define     SL1(a)          SF("%lld",&a);
#define     SL2(a,b)        SF("%lld%lld",&a,&b);
#define     SL3(a,b,c)      SF("%lld%lld%lld",&a,&b,&c);
#define     SL4(a,b,c,d)    SF("%lld%lld%lld%lld",&a,&b,&c,&d);
#define     SL5(a,b,c,d,e)  SF("%lld%lld%lld%lld%lld",&a,&b,&c,&d,&e);
#define     PL1(a)          PF("%lld ",a);
#define     PL2(a,b)        PF("%lld %lld ",a,b);
#define     PL3(a,b,c)      PF("%lld %lld %lld ",a,b,c);
#define     PL4(a,b,c,d)    PF("%lld %lld %lld %lld ",a,b,c,d);
#define     PL5(a,b,c,d,e)  PF("%lld %lld %lld %lld %lld ",a,b,c,d,e);
#define     CHK(a)          cerr << #a << "=" << a << " ";
#define     C1(a)           cerr << "{ "; CHK(a) cerr << "} ";
#define     C2(a,b)         cerr << "{ "; CHK(a) CHK(b) cerr << "} ";
#define     C3(a,b,c)       cerr << "{ "; CHK(a) CHK(b) CHK(c) cerr << "} ";
#define     C4(a,b,c,d)     cerr << "{ "; CHK(a) CHK(b) CHK(c) CHK(d) cerr << "} ";
#define     C5(a,b,c,d,e)   cerr << "{ "; CHK(a) CHK(b) CHK(c) CHK(d) CHK(e) cerr << "} ";
#define     PAIR(T,A,a,B,b) struct T{A a;B b;T(){};T(A x,B y){a=x;b=y;} BO<(T z)const{return a!=z.a?a<z.a:b<z.b;}}
#define     FOR(a,b,c)      for(int a=b;a<=c;a++)
#define     ROF(a,b,c)      for(int a=b;a>=c;a--)
#define     SALL(a,b)       FOR(i,1,b)S1(a[i])
#define     SALL2(a,b,c)    FOR(i,1,b)FOR(j,1,c)S1(a[i][j])
#define     PALL(a,b)       FOR(i,1,b)P1(a[i])EL
#define     PALL2(a,b,c)    FOR(i,1,b){FOR(j,1,c)P1(a[i][j])EL}EL
#define     SLALL(a,b)      FOR(i,1,b)SL1(a[i])
#define     SLALL2(a,b,c)   FOR(i,1,b)FOR(j,1,c)SL1(a[i][j])
#define     PLALL(a,b)      FOR(i,1,b)PL1(a[i])EL
#define     PLALL2(a,b,c)   FOR(i,1,b){FOR(j,1,c)PL1(a[i][j])EL}EL
#define     EL              PF("\n");
#define     CEL             cerr << "\n";
#define     LINE            cerr << "--------------------\n";
#define     MSET(a,b)       memset(a,b,sizeof(a));
#define     LL              long long
#define     BO              bool operator
#define     MP              make_pair
#define     IB              push_back
#define     IF              push_front
#define     DB              pop_back()
#define     DF              pop_front()
#define     LB              lower_bound
#define     UB              upper_bound
#define     _1              first
#define     _2              second
#define     SEED            srand(time(NULL));
#define     MAXPQ(T)        priority_queue<T>
#define     MINPQ(T)        priority_queue<T,vector<T>,greater<T>>
#define     READ(a)         freopen(a,"r",stdin);
#define     WRITE(a)        freopen(a,"w",stdout);
#define     BASE            257
#define     MOD             1000000007
#define     MOD2            1000000009
#define     INF             2000000000
#define     PI              3.141592653589793
template<typename A, typename B> inline bool mins(A &x,B y){return (x>y)?(x=y,1):0;}
template<typename A, typename B> inline bool maxs(A &x,B y){return (x<y)?(x=y,1):0;}
using namespace std;

int _,ans,fail,n,r,c;
int N[101][101],E[101][101],S[101][101],W[101][101];
char s[101][101];

int main(){
    //READ("A-small-attempt0.in")
    READ("A-large.in")
    WRITE("outAl.txt")
    S1(_)
    FOR(__,1,_){
        S2(r,c)
        FOR(i,1,r){
            FOR(j,1,c){
                SF(" %c",&s[i][j]);
                N[i][j]=0;
                E[i][j]=0;
                S[i][j]=0;
                W[i][j]=0;
            }
        }
        ans=0; fail=0;
        FOR(i,1,r){
            FOR(j,1,c){
                if(s[i][j]!='.'){
                    ROF(k,i-1,1){
                        if(s[k][j]!='.'){
                            N[i][j]=1;
                            break;
                        }
                    }
                    FOR(k,i+1,r){
                        if(s[k][j]!='.'){
                            S[i][j]=1;
                            break;
                        }
                    }
                    ROF(k,j-1,1){
                        if(s[i][k]!='.'){
                            W[i][j]=1;
                            break;
                        }
                    }
                    FOR(k,j+1,c){
                        if(s[i][k]!='.'){
                            E[i][j]=1;
                            break;
                        }
                    }
                    if( (s[i][j]=='^' and N[i][j]==0) or (s[i][j]=='v' and S[i][j]==0) or (s[i][j]=='>' and E[i][j]==0) or (s[i][j]=='<' and W[i][j]==0) ){
                        if(N[i][j]||E[i][j]||S[i][j]||W[i][j]){
                            ans++;
                        }
                        else{
                            fail=1;
                        }
                    }
                }
            }
        }
        PF("Case #%d: ",__);
        if(fail){
            PF("IMPOSSIBLE");
        }
        else{
            P1(ans)
        }
        EL
    }
    return 0;
}
