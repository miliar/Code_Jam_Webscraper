#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int T;
    double C, F, X;
    int i;
    cin>>T;
    double ans;
    double rate;
    bool flag ;
    for(i=0;i<T;++i)
    {
        ans = 0;
        rate = 2;
        flag = 1;
        cin>>C>>F>>X;
        if(X<=C)
            ans = X/rate ;
        else
        {
            while(flag)
            {
                ans += C/rate;
               // cout<<ans<<endl;
                if(F*X > (F+rate)*C)
                {
                    rate = rate + F;
                }
                else
                {
                    flag = 0;
                }
            }
            ans +=(X-C)/rate;
        }
        cout<<"Case #"<<i+1<<": ";
        printf("%.7f\n", ans);
    }
    return 0;
}
