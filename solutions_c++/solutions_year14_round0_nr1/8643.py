#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>
#include <unistd.h>
#include <stdint.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>

#define Sd(t)   scanf("%d",&t)
#define Slld(t) scanf("%lld",&t)
#define Ss(t)   scanf("%s",t)
#define Slf(t)  scanf("%lf",&t)

#define Pd(t)   printf("%d",t)
#define Plld(t) printf("%lld",t)
#define Ps(t)   printf("%s",t)
#define Plf(t)  printf("%lf",t)

#define Pc(t)    printf("%c",t)
#define Pn       printf("\n")
#define MOD 1000000007
#define MX 10000

using namespace std;
int main(){
    int T,ans1,ans2,op[17];
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    Sd(T);
    REP(cs,T){
        REP(i,17){
            op[i] = 0;
        }
        Sd(ans1);
        REP(i,4){
            int t;
            if(i+1 == ans1) {
                REP(i,4){
                    Sd(t);
                    op[t] = 1;
                }
            }
            else {
                REP(i,4){
                    Sd(t);
                }
            }
        }
        int cnt = 0,save = -1;
        Sd(ans2);
        REP(i,4){
            int t;
            if(i+1 == ans2) {
                REP(i,4){
                    Sd(t);
                    if(op[t] == 1){
                        cnt++;
                        save = t;
                    }

                }
            }
            else {
                REP(i,4){
                    Sd(t);
                }
            }
        }
        printf("Case #%d: ",cs+1);
        if(cnt == 1){
            Pd(save);
        }
        else if(cnt > 1){
            Ps("Bad magician!");
        }
        else{
            Ps("Volunteer cheated!");
        }
        Pn;
    }
    return 0;
}
