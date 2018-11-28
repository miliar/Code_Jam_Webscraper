#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long LL;
LL gcd(LL a,LL b){
    if (b==0) return a;
    return gcd(b,a%b);
}


int main()
{
    freopen("A-small-attempt0 (2).in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    LL p,q;
    int P,Q;
    char c;
    int cas=0;
    scanf("%d",&T);
    while (T--){
        scanf("%d/%d",&P,&Q);
        p=(LL)P;
        q=(LL)Q;
        LL g=gcd(p,q);
        p=p/g;
        q=q/g;
        //cerr<<__builtin_popcount(q)<<endl;
        if (__builtin_popcount(q)!=1){
            printf("Case #%d: impossible\n",++cas);
            continue;
        }
        int ans=0;
        for (int i=0;i<40;i++){
            if (p>=q) break;
            p*=2;
            ans++;
        }
        if (p>=q) printf("Case #%d: %d\n",++cas,ans);
        else printf("Case #%d: impossible\n",++cas);
    }
    return 0;
}
