#include <cstdio>
#define fi "B.inp"
#define fo "B.out"
using namespace std;
double c,f,x;
int t;
double l,m,r,wait;
int main(){
    freopen(fi,"r",stdin);
    freopen(fo,"w",stdout);
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        scanf("%lf%lf%lf",&c,&f,&x);
        wait=0;
        r=2.0;
        l=x/2;
        while (1){
            wait=wait+c/r;
            r=r+f;
            m=wait+x/r;
            if (m>l) break;
            l=m;
        }
        printf("%.7lf\n",l);
    }
    return 0;
}

