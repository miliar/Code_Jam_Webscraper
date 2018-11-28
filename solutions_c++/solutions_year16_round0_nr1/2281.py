#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,k,n,t,a,b,c;
    for(scanf("%d",&t),i=1;i<=t;++i){
        scanf("%d",&n);
        if(!n) printf("Case #%d: INSOMNIA\n",i);
        else{
            for(k=1,a=0,b=(1<<10)-1;a!=b;++k)
                for(c=k*n;c;a|=1<<(c%10),c/=10);
            printf("Case #%d: %d\n",i,(k-1)*n);
        }
    }
    return 0;
}
