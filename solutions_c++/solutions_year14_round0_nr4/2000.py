#include<cstdio>
#include<algorithm>
using namespace std;
int T,n,ac1,ac2,p,q,u[1005],ok;
double a[1005],b[1005];
int main(){
    scanf("%d",&T);
    for (int o=1; o<=T; o++){
        scanf("%d",&n);
        for (int i=1; i<=n; i++) scanf("%lf",&a[i]);
        for (int i=1; i<=n; i++) scanf("%lf",&b[i]);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        q=1; ac1=ac2=0;
        for (int i=1; i<=n; i++){
            if (a[i]>b[q]) ++ac1,++q;
        }
        for (int i=1; i<=n; i++) u[i]=1;
        for (int i=1; i<=n; i++){
            ok=1;
            for (int j=1; j<=n; j++){
                if ((b[j]>a[i])&&u[j]){
                    u[j]=0;
                    ok=0;
                    break;    
                }
            }
            if (ok) ++ac2;
        }
        printf("Case #%d: %d %d\n",o,ac1,ac2);
    }
    return 0;    
}
