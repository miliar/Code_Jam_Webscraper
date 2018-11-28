#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T;
int n,m,l;
unsigned long long a[2000], b[2000], c[2000], org;
unsigned long long nc[4000], pos[4000], cost;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d", &T);
    for(int cs=1;cs<=T;++cs){
        printf("Case #%d: ",cs);
        scanf("%d%d", &n,&m);

        org = 0;
        for(int i=0; i<m; ++i){
            scanf("%d %d %d", a+i, b+i, c+i);
            pos[i]=a[i]; pos[i+m]=b[i];
            unsigned long long tmp = (n+n-(b[i]-a[i]-1))*(b[i]-a[i])/2;
            org += tmp*c[i];
        }

        memset(nc, 0, sizeof(nc));
        sort(pos,pos+m+m);
        l = unique(pos, pos+m+m)-pos;
        for(int i=0; i<m; ++i){
            int x = lower_bound(pos, pos+l, a[i]) - pos;
            int y = lower_bound(pos, pos+l, b[i]) - pos;
            for(int j=x; j<y; ++j)
                nc[j] += c[i];
        }

        cost = 0;
        int p=0;
        while(p<l){
            unsigned long long mm = 10000000000, tmp;
            int q = p;
            while(nc[q] != 0 && q<l){
                if(mm>nc[q]) mm = nc[q];
                ++q;
            }
            tmp = (n+n-(pos[q]-pos[p]-1))*(pos[q]-pos[p])/2;
            cost += tmp*mm;
            for(int i=p; i<q; ++i)
                nc[i] -= mm;

            while(nc[p]==0 && p<l) ++p;
        }

        printf("%lld\n", org-cost);
    }
}
