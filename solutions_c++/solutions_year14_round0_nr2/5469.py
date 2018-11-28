#include <cstdio>
#include <iostream>

using namespace std;

double c, f, x, ans, p, tt;

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> c >> f >> x;
        p = 2.0;
        ans = x / p;
        tt = 0.0;
        for(;;){
            tt += c / p;
            p += f;
            if(ans < tt + x / p)
                break;
            else
                ans = tt + x / p;

        }
        printf("Case #%d: %.7lf\n",t,ans);
    }
    return 0;
}
