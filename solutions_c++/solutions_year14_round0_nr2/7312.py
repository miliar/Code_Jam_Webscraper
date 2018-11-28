#include <cstdio>

using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k;
    double c,f,x;
    double s;
    double ans;
    scanf("%d",&t);

    for(k=1;k<=t;k++) {
        scanf("%lf %lf %lf",&c,&f,&x);
        ans = 0;
        s = 2;
        while(x/s > c/s+(x/(s+f))) {
            ans += c/s;
            s += f;
        }
        ans += x/s;
        printf("Case #%d: %.7lf\n",k,ans);
    }
    return 0;
}
