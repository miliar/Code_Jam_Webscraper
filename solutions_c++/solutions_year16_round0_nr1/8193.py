#include<cstdio>
#include<queue>
#include<climits>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<ctype.h>
#include<set>
#include<vector>
#include<map>
#include<time.h>
#include<list>
#include<stack>
using namespace std;
#define mod 1000000007
#define mem(x) memset(x,0,sizeof(x))
#define pri printf
#define sca scanf

typedef long long LL;
const double PI=acos(-1.0);
const double  eps=1e-9;

int main(){
    int n,i,j,m,k;
    int T;
    freopen("A-large.txt","r",stdin);
    freopen("A-large.out","w",stdout);
    sca("%d",&T);
    bool f[10];
    for (int cas=1;cas<=T;cas++){
        sca("%d",&n);
        if (n==0) {
            pri("Case #%d: INSOMNIA\n",cas);
            continue;
        }
        m=n;
        memset(f,0,sizeof f);
        k=0;
        while (n%m==0){
           for (j=1;j<=1000000000&&j<=n;j*=10){
                if (f[n/j%10]==0) {
                    f[n/j%10]=1;
                    k++;
                }
                if (k==10) {
                    break;
                }
           }
           if (k==10) break;
           n+=m;
        }
        pri("Case #%d: %d\n",cas,n);
    }
    return 0;
}





















