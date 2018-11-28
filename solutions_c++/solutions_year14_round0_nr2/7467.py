#include <string.h>
#include <iomanip>
#include <iostream>
#include <stdio.h>
using namespace std;
double C,F,X;
int main()
{
    cout.setf(ios::fixed);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        cin>>C>>F>>X;
        double per=2.0;
        double res=X/per;
        if(C >= X)
            cout<<"Case #"<<cas++<<": "<<setprecision(7)<<res<<endl;
        else
        {
            res=C/per;
            while(1)
            {
                if((X-C)/per <= X/(per+F))
                {
                    res+=(X-C)/per;
                    break;
                }
                else
                {
                    per+=F;
                    res+=C/per;
                }
            }
            cout<<"Case #"<<cas++<<": "<<setprecision(7)<<res<<endl;
        }
    }
    return 0;
}
