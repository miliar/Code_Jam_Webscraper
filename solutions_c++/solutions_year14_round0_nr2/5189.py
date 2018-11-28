#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("B_small.in","r",stdin);
    freopen("B_small.out","w",stdout);

    int test,CS=0,i,j;
    double C,F,X,factor,timeCnt,ans;

    cin>>test;
    while(test--) {
        cin>>C>>F>>X;
        timeCnt = 0;
        factor = 2;
        ans = X/2+1;
        while(true) {
            if(timeCnt+X/factor < ans) {
                ans = timeCnt + X/factor;
                timeCnt = timeCnt+C/factor;
                factor += F;
            } else {
                break;
            }
        }
        cout.precision(10);
        cout<<"Case #"<<++CS<<": "<<ans<<endl;
    }

    return 0;
}
