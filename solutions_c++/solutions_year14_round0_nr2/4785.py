#include <iostream>
#include <stdio.h>
using namespace std;
#define eps 1e-7
double answer(double a,double b,double c)
{
    double ans=0;
    double v=2;
    while(1)
    {

        if((ans+a/v+c/(v+b)+eps)<(ans+c/v))
        {
            ans+=a/v;
            v=v+b;
        }
        else
        {
            ans=ans+c/v;
            printf("%.7lf\n",ans);
            break;
        }
    }
}
int main()
{
    //freopen("0.in","r",stdin);
    //freopen("0.out","w",stdout);
    double C,F,X;
    int N;
    cin>>N;
    for(int i=0; i<N; i++)
    {
        cin>>C>>F>>X;
        cout<<"Case #"<<(i+1)<<": ";
        answer(C,F,X);
    }
    return 0;
}
