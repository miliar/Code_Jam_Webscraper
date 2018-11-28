#include    <stdio.h>
#include    <iostream>
#include    <queue>
#include    <stack>
#include    <deque>
#include    <list>
#include    <vector>
#include    <map>
#include    <set>
#include    <cmath>
#include    <ctime>
#include    <string.h>
#include    <algorithm>
#define     SF              scanf
#define     S1(a)           SF("%d",&a);
#define     S2(a,b)         SF("%d%d",&a,&b);
#define     S3(a,b,c)       SF("%d%d%d",&a,&b,&c);
#define     S4(a,b,c,d)     SF("%d%d%d%d",&a,&b,&c,&d);
#define     S5(a,b,c,d,e)   SF("%d%d%d%d%d",&a,&b,&c,&d,&e);
#define     SL1(a)          SF("%lld",&a);
#define     SL2(a,b)        SF("%lld%lld",&a,&b);
#define     SL3(a,b,c)      SF("%lld%lld%lld",&a,&b,&c);
#define     SL4(a,b,c,d)    SF("%lld%lld%lld%lld",&a,&b,&c,&d);
#define     SL5(a,b,c,d,e)  SF("%lld%lld%lld%lld%lld",&a,&b,&c,&d,&e);
#define     SFC(a)          SF(" %c",&a);
#define     SFS(a)          SF("%s",a);
#define     PF              printf
#define     P1(a)           PF("%d ",a);
#define     P2(a,b)         PF("%d %d ",a,b);
#define     P3(a,b,c)       PF("%d %d %d ",a,b,c);
#define     P4(a,b,c,d)     PF("%d %d %d %d ",a,b,c,d);
#define     P5(a,b,c,d,e)   PF("%d %d %d %d %d ",a,b,c,d,e);
#define     PL1(a)          PF("%lld ",a);
#define     PL2(a,b)        PF("%lld %lld ",a,b);
#define     PL3(a,b,c)      PF("%lld %lld %lld ",a,b,c);
#define     PL4(a,b,c,d)    PF("%lld %lld %lld %lld ",a,b,c,d);
#define     PL5(a,b,c,d,e)  PF("%lld %lld %lld %lld %lld ",a,b,c,d,e);
#define     PFC(a)          PF("%c",a);
#define     PFS(a)          PF("%s",a);
#define     CHK(a)          cout << #a << " " << a << " ";
#define     C1(a)           PF("{ "); CHK(a) PF("} ");
#define     C2(a,b)         PF("{ "); CHK(a) CHK(b) PF("} ");
#define     C3(a,b,c)       PF("{ "); CHK(a) CHK(b) CHK(c) PF("} ");
#define     C4(a,b,c,d)     PF("{ "); CHK(a) CHK(b) CHK(c) CHK(d) PF("} ");
#define     C5(a,b,c,d,e)   PF("{ "); CHK(a) CHK(b) CHK(c) CHK(d) CHK(e) PF("} ");
#define     SP              PF(" ");
#define     EL              PF("\n");
#define     LINE            PF("--------------------\n");
#define     F0(a,b)         for(int a=0;a<=b;a++)
#define     R0(a,b)         for(int a=b;a>=0;a--)
#define     F1(a,b)         for(int a=1;a<=b;a++)
#define     R1(a,b)         for(int a=b;a>=1;a--)
#define     FV(a,b)         for(int a=0;a<v[b].size();a++)
#define     RV(a,b)         for(int a=0;a<rv[b].size();a++)
#define     STR(a)          #a
#define     ABS(a)          (a)>=0 ? (a) : -(a);
#define     LL              long long
#define     BO              bool operator
#define     MP              make_pair
#define     IB              push_back
#define     IF              push_front
#define     DB              pop_back()
#define     DF              pop_front()
#define     LB              lower_bound
#define     UB              upper_bound
#define     FI              first
#define     SC              second
#define     QT              Q.top()
#define     QF              Q.front()
#define     QB              Q.back()
#define     ST              S.top()
#define     SZ              size()
#define     PQ              priority_queue
#define     IT              iterator
#define     PII             pair<int,int>
#define     PLL             pair<LL,LL>
#define     MII             map<int,int>
#define     MLL             map<LL,LL>
#define     FRI(a)          freopen(a,"r",stdin);
#define     FRO(a)          freopen(a,"w",stdout);
#define     BF              100000
#define     MOD             1000000007
#define     INF             2000000000
#define     LINF            9000000000000000000
#define     PI              3.141592653589793
#define     debug           if(DEBUG)
#define     DEBUG           0
using namespace std;

int t,n,m[1001],s1,s2,mx;

int main(){
    //FRI("A-small-attempt0.in")
    FRI("A-large.in")
    FRO("out.txt")
    S1(t)
    F1(tc,t){
        S1(n)
        F1(i,n){
            S1(m[i])
        }
        s1=0; s2=0; mx=0;
        F1(i,n-1){
            if(m[i]-m[i+1]>0){
                s1+=m[i]-m[i+1];
                mx=max(mx,m[i]-m[i+1]);
            }
        }
        F1(i,n-1){
            s2+=min(mx,m[i]);
        }
        PF("Case #%d: %d %d\n",tc,s1,s2);
    }
    return 0;
}
