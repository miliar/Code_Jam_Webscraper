#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
int main(){
    int t;
    double c,f,x,r,r1,init,dest,ans;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
            r=2.0;
            cin>>c>>f>>x;
            ans=x/r;
            r1=f+2.0;
            init=c/r;
            dest=init+c/r1;
            r+=f;
            r1+=f;
            while((init + x/ r)>(dest + x/ r1))
            {
             init=init+c/r;
             dest=dest+c/r1;
             r+=f;
             r1+=f;
             }
             printf("Case #%d: ",k);
             printf("%.7lf\n",min(ans,init + x/ r));
    }
    return 0;
}
