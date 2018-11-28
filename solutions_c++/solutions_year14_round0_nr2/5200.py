#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    long long int t1;
    cin>>t1;

    for(long long int e=1;e<=t1;e++)
    {
         double c,f,x,t=0.0,a=0.0,r=2;
        cin>>c>>f>>x;

        while(a!=x)
        {

            if((x/r)<(c/r + (x/(r+f))))
            {

                a=x;
                t=t+x/r;
                break;
            }else
            {
            a=0;
            t=t+c/r;
            r=r+f;
            }
        }
        printf("Case #%lld: %.7lf \n",e,t);
    }

}
