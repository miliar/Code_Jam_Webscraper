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
#include <unordered_map>
#define REP(i,n) for(int (i)=0;i<(int)(n);++(i))
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define PB push_back
#define FT first
#define SD second
#define ZERO(x) memset(x,0,sizeof(x))
#define NEG(x) memset(x,-1,sizeof(x))
#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d%d",&(x),&(y))
#define RIII(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define OIII(x,y,z) printf("%d %d %d\n",(x),(y),(z))
#define OII(x,y) printf("%d %d\n",(x),(y))
#define OI(x) printf("%d\n",(x))
#define OL(x) cout<<(x)<<endl
#define OLL(x,y) cout<<(x)<<" "<<(y)<<endl
#define OLLL(x,y,z) cout<<(x)<<" "<<(y)<<" "<<(z)<<endl
#define RS(s) scanf("%s",(s))
#define MP(x,y) make_pair((x),(y))
#define SZ(x) ((int)(x).size())
#define FIN(f) freopen(f,"r",stdin)
#define FOUT(f) freopen(f,"w",stdout)
typedef long long LL;
using namespace std;
typedef pair<int,int> PII;
const int INF = 1<<28;
const int MOD = 1e9+7;
const int maxn = 111;
int main(int argc, char const *argv[])
{
    int T;
    RI(T);
    for(int kase=1;kase<=T;++kase) {
        LL n;
        cin>>n;
        vector<bool> h(10,0);
        int cnt = 10;
        LL l = n;
        for(LL i=1;i<=1000001;++i) {
            LL x = i * n;
            l = x;
            while(x) {
                int d = x%10;
                x/=10;
                if(!h[d]){
                    h[d] = 1;
                    cnt--;
                }
            }
            if(cnt==0)break;
        }
        if(cnt)printf("Case #%d: INSOMNIA\n",kase);
        else printf("Case #%d: %lld\n",kase, l);
    }
    return 0;
}