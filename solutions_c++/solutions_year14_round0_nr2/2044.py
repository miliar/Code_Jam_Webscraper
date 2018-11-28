#include <bits/stdc++.h>
#define mp make_pair
using namespace std;
double C,F,X,V;
main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++){
        printf("Case #%d: ",test);
        cin>>C>>F>>X;
        double ans;
        V=2.0;
        if(C>=X) ans=X/V;
        else{
            ans=C/V;
            while((X-C)/V>X/(V+F)){
                V=V+F;
                ans=ans+C/V;
            }
            ans=ans+(X-C)/V;
        }
        printf("%.7lf\n",ans);
    }
}
