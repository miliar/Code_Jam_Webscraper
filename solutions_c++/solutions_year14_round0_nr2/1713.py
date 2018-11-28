#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <climits>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#define REP(i,n) for( int (i)=0;(i)<(int)(n); ++(i))
#define REPR(i,n) for( int (i) = n; (i)>=0; --(i))
#define REPN(i,x,y) for( int i = x; (i) < (int)(y); (i)++ )
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define ZERO(x) memset(x,0,sizeof(x))
#define NEG(x) memset(x,-1,sizeof(x))
#define SZ(x) (int)(x).size()
#define RI(n) scanf("%d",&(n))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RS(x) scanf("%s",x)
#define OI(x) printf("%d\n",(x))
#define OII(x,y) printf("%d %d\n",(x),(y))
#define MP(x,y) make_pair((x),(y))
#define FT first
#define SD second
#define PB push_back
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
LL LLMAX = 9223372036854775807LL;
const int MOD = 1000000007;
const int maxn = 500+10;
double C,F,X;
bool ok(double M){
    double rem = M;
    double cur=0,cr = 2;
    while(rem>1e-8){
        if( (X-cur) < rem*cr)return 1;
        else{
            if(rem*cr<C)return 0;
            rem -= C/cr;
            cr += F;
        }
    }
}
int main()
{
#ifndef ONLINE_JUDGE
    //freopen("in.txt","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
    int T;
    RI(T);
    for(int kase = 1;kase<=T;++kase){
        scanf("%lf%lf%lf",&C,&F,&X);
        double L=0,R = X;
        while(R-L>1e-10){
            double M = (R+L)/2.0;
            if(ok(M))R = M;
            else L = M;
        }
        printf("Case #%d: %.7lf\n",kase,L);
    }
}


