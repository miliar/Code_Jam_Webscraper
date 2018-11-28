#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<fstream>
using namespace std;

int main()
{
    int T,ics=0;
    double c,f,x,t0,t,t1,t2,sum,r;
   // freopen("B-small-attempt0.in","r",stdin);
   // freopen("B-small-attempt0.out","w",stdout);
    cin>>T;
    while(T--){
        cin>>c>>f>>x;
        sum=0;
        r=2.0;
        t0=x/r;
        t=0;
        while(sum<x){
            if(x-sum<=c){
                t=t+(x-sum)/r;
                break;
            }
            t1=(x-sum)/r;
            t2=c/r+(x-sum)/(r+f);
            if(t1<t2){
                t+=t1;
                sum=x;

            }else {
                t+=c/r;
                r+=f;
            }
        }
        printf("Case #%d: %.7lf\n",++ics,min(t,t0));
    }
    return 0;
}
