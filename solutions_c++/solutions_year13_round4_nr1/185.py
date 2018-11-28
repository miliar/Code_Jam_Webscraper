// @author peter50216
// #includes {{{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<functional>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<vector>
#include<iostream>
#include<sstream>
using namespace std;
// }}}
// #defines {{{
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)
#define REPL(i,x) for(int i=0;x[i];i++)
#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define DRIII(x,y,z) int x,y,z;RIII(x,y,z)
#define RS(x) scanf("%s",x)
#define PI(x) printf("%d\n",x)
#define PIS(x) printf("%d ",x)
#define CASET int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define MP make_pair
#define PB push_back
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,-1,sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define F first
#define S second
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
// }}}

const int mod=1000002013;
inline int loss(int d){
    return (d*(d-1LL)/2)%mod;
}
pair<int,PII> all[2010];
int stk[2010],sc;
int main(){
    CASET{
        DRII(n,m);
        int ac=0;
        long long ol=0,nl=0;
        while(m--){
            int a,b,p;
            RIII(a,b,p);
            ol=(ol+loss(b-a)*p)%mod;
            all[ac++]=MP(a,MP(0,p));
            all[ac++]=MP(b,MP(1,p));
        }
        sort(all,all+ac);
        sc=0;
        for(int i=0;i<ac;i++){
            if(all[i].S.F==0)stk[sc++]=i;
            else{
                int p=all[i].S.S;
                while(p>0){
                    int j=stk[sc-1];
                    int pp=all[j].S.S;
                    if(p<pp){
                        all[j].S.S-=p;
                        nl=(nl+p*(LL)loss(all[i].F-all[j].F))%mod;
                        p=0;
                    }else{
                        sc--;
                        nl=(nl+pp*(LL)loss(all[i].F-all[j].F))%mod;
                        p-=pp;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",cas++,(int)((nl-ol+mod)%mod));
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

