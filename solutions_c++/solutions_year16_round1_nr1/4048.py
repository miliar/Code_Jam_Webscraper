/*input
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE

*/
#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;
long long mod=1e9+7;
 
typedef long long unsigned llu;
typedef long long int lld;
typedef long ld;
#define rep(i,a,n) for(long long int i = (a); i <= (n); ++i)
#define repI(i,a,n) for(int i = (a); i <= (n); ++i)
#define repD(i,a,n) for(long long int i = (a); i >= (n); --i)
#define repDI(i,a,n) for(int i = (a); i >= (n); --i)
 
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld%lld",&a,&b)
#define sc3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define scd(a) scanf("%d",&a)
#define scd2(a,b) scanf("%d%d",&a,&b)
#define scd3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scf(a) scanf("%lf",&a)
#define scf2(a,b) scanf("%lf%lf",&a,&b)
#define scf3(a,b,c) scanf("%lf%lf%lf",&a,&b,&c)
#define prL(a) printf("%lld\n",a)
#define prS(a) printf("%lld ",a)
#define prdL(a) printf("%d\n",a)
#define prdS(a) printf("%d ",a)
#define prfL(a) printf("%lf\n",a)
#define prfS(a) printf("%lf ",a)
#define popcount __builtin_popcountll
#define swap(a,b,t) t=a;a=b;b=t
typedef pair<lld,lld> PA;
 
#define lim 1000003
#define lim2 1003
inline lld sqr(lld x) { return x * x; }
// map<pair<PA,PA>,lld> M;
// map<string,lld> M,My;
// map<PA,lld> Ms;
// deque<PA> Q;
// map<lld,lld>::iterator it;
// std::ios::sync_with_stdio(false);
 
// multiset<lld> S;
// set<lld> S;
// vector<lld> V[lim];
 
// bool dp[1002][12][12];
// priority_queue<PA> Q;
// lld A[lim],B[lim],C[lim];
lld A[lim];
// lld X[lim],Y[lim];
// PA P[lim];
// lld dp[1<<18];
lld one,zero,ansR,numNodes;

lld findGcd(lld a,lld b){
    if(a==0) return b;
    else return findGcd(b%a,a);
}
lld powP(lld a,lld b){
    if(b==0) return 1%mod;
    lld k;
    k=powP(a,b/2);
    k=k*k%mod;
    if(b%2==0) return k;
    else return a*k%mod;
}

char B[lim];

int main(){
    // std::ios::sync_with_stdio(false);
    lld T,i,j,h,l,r,k,s,b,c,a,d,q,p,n,m,w,x,y,v,z,t,curr,prev,sum,ans,pos,val,countA,secondMin,indicator;
    sc(T);
    rep(testCase,1,T){
        string S;
        cin>>S;
        a=2003;
        B[a]=S[0];
        b=2004;
        n=S.size();
        rep(i,1,n-1){
            if(S[i]<B[a]){
                B[b]=S[i];
                b++;
            }
            else{
                a--;
                B[a]=S[i];
            }
        }
        printf("Case #%lld: ",testCase);
        rep(i,a,b-1) printf("%c",B[i] );
        printf("\n");
    }
    return 0;
}
