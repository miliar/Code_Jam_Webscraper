#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    cin >>T;
    for(int x=1;x<=T;x++)
    {
        long double C,F,X,y=0,t[100001];
        cin >>C>>F>>X;
        t[0]=X/2;
        for(int i=1;;i++)
        {
            t[i]=X/(i*F+2);
            for(int j=0;j<i;j++)
                t[i]+=C/(2+j*F);
            if(t[i]<t[i-1])
                y=t[i];
            else
            {
                y=t[i-1];
                break;
            }
        }
        cout <<"Case #"<<x<<": "<<fixed<<setprecision(7)<<y<<endl;
    }
    return 0;
}
