#include<iostream>
#include<cstdio>
using namespace std;

int main() {
    freopen("CookieClickerAlpha.in","r",stdin);
    freopen("CookieClickerAlpha.out","w",stdout);
    double C,F,X,ans,per,now;
    int T,cas=1;
    cin >> T;
    while(T--) {
        cin >> C >> F >> X;
        per = 2.0;now = 0.0;
        ans = 0.0;
        while(1) {
            //cerr << "per " << per << endl;
            if(X/per > C/per+X/(per+F)){
                ans += C/per;
                per += F;
            }else {
                ans += X/per;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",cas++,ans);
    }
    return 0;
}
