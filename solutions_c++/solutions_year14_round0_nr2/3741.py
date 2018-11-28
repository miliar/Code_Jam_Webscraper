#include <cstdio>
#include <iostream>
#include <cstring>
#include <iostream>

using namespace std;

int main()
{
   // freopen("B-small-attempt0.in","r",stdin);
   // freopen("ans2small.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    freopen("ans2large.txt","w",stdout);
    double C,T,F,X;
    int ncase = 0;
    cin>>T;
    while(T--){
        cin>>C>>F>>X;
        ncase++;
        double ans = 0;
        double v = 2;
        double now = 0;
        while(now+C<X){
            ans+= C/v;
            now+=C;
            double t1 = (X-now)/v;
            double t2 = C/F;
            if(t1<t2){
                now = X;
                ans += t1;
                break;
            }
            else{
                now -= C;
                v += F;
            }
        }
        if(now<X) ans += (X-now)/v;
        printf("Case #%d: %.7lf\n",ncase,ans);
    }
    return 0;
}
