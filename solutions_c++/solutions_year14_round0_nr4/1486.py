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
const int maxn = 1000+10;
double a[maxn],b[maxn];

int main()
{
#ifndef ONLINE_JUDGE
    //freopen("in.txt","r",stdin);
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
    int T;
    RI(T);
    for(int kase = 1;kase<=T;++kase){
        int n;
        RI(n);
        REP(i,n)scanf("%lf",&a[i]);
        REP(i,n)scanf("%lf",&b[i]);

        sort(a,a+n);
        sort(b,b+n);

        int am=0,aM=n-1,bm=0,bM=n-1;
        int cnt=0;
        for(int i=0;i<n;++i){
            if(b[bM]>a[aM]){
                bM--;aM--;
            }
            else if(b[bM]<a[aM]){
                cnt++;
                bm++;aM--;
            }
            else;
        }

        int c2=0;
        am=0,aM=n-1,bm=0,bM=n-1;
        for(int i=0;i<n;++i){
            if(b[bM]>a[aM]){
                am++;bM--;
            }
            else{
                aM--;bM--;c2++;
            }
        }

        printf("Case #%d: %d %d\n",kase,c2,cnt);
    }
}


