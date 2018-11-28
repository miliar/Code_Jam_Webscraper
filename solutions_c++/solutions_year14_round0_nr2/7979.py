#include <cstdio>
#include <cstring>
using namespace std;

int main(){
    freopen("1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tt, cas=0;
    double C,F,X;
    scanf("%d",&tt);
    while(tt--){
        printf("Case #%d: ", ++cas);
        scanf("%lf%lf%lf",&C,&F,&X);
        if(C>=X){
            printf("%.7f\n", X/2);
            continue;
        }
        double ans = 0;
        double now = 2;
        while(1){
            if(C/now+X/(now+F) <= X/now){
                ans += C/now;
                now += F;
            }
            else{
                ans += X/now;
                break;
            }
        }
        printf("%.7f\n", ans);
    }
    return 0;
}
