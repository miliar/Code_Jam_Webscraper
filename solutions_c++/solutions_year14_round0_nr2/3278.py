#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int t,T;
    double C,F,X;
    double timeSoFar;
    double p; // Current Production Rate
    double q; // Future Production Rate
    double cookieCount;
    scanf("%d",&T);
    //cout<<T<<endl;
    for(t=1;t<=T;t++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);

        timeSoFar=0;
        cookieCount=0;
        p=2;
        q=2+F;
        while(1)
        {
            if(   (  (   C/p   )   +   (   X/q   )   )<(   X/p   )   )
            {
                timeSoFar+=C/p;
                //cout<<p<<endl;
                //printf("<%f\n",timeSoFar);
                p=p+F;
                q=q+F;
            }
            else //if(   (  (   C/p   )   +   (   X/q   )   )>(   X/p   )   )
            {
                timeSoFar+=(X/p);
                //printf(">%f\n",timeSoFar);
                break;
            }
        }
        printf("Case #%d: %.7lf\n",t,timeSoFar);

    }
    return 0;
}
