#include <cstdio>
#include <iostream>
using namespace std;
const double esp = 1e-9;
int main(){
    double ans, x, f, c,s;
    int t,nc = 0;
   freopen("B-large.in","r",stdin);
    freopen("bout.out","w",stdout);
    cin >> t;
    while (t--){
        s = 2;
        ans = 0;
        scanf("%lf%lf%lf",&c,&f,&x);
        while(c*(s+f) < x * f){
           ans += c / s;
           s += f;
        }
        ans += x / s;
        printf("Case #%d: %.7f\n",++nc,ans);
    }
    return 0;

}
