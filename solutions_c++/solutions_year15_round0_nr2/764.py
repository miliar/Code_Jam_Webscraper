#include <cstdio>
#include <algorithm>
using namespace std;
bool cmp(int p,int q){
    return p>q;
}
int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t,k=0,d,p[1005],i,j,m,sum;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&d);
        for(i=0;i<d;i++) scanf("%d",&p[i]);
        std::sort(p,p+d,cmp);
        m=p[0];
        for(j=2;j<m;j++){
            for(sum=i=0;i<d;i++)
                sum+=(p[i]-1)/j;
            m=min(m,sum+j);
        }
        printf("Case #%d: %d\n",++k,m);
    }
}
