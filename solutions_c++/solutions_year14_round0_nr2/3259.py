#include <iostream>
#include <cstdio>

using namespace std;

#define DEBUG

int main()
{
    #ifdef DEBUG
    freopen("a.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    #endif

    int tc,i;
    double c,f,x,t,co;
    cin>>tc;
    for(i=1;i<=tc;i++) {
        cin>>c>>f>>x;
        co=2;
        t=0;
        while(1) {
            if((x/co)>((c/co)+(x/(co+f)))) {
                t+=c/co;
                co+=f;
            } else {
                t+=x/co;
                break;
            }
        }
        printf("Case #%d: %0.7lf\n",i,t);
    }

    return 0;
}
