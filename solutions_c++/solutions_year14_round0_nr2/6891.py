#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int t;
    double a,b,c,d,e,f;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        double rate=2,ti=0;
        cout<<"Case #" << i << ": ";
        cin>>a>>b>>c;
        while(1)
        {
            if(c/(rate+b)+a/rate<c/rate)
            {
                ti+=a/rate;
                rate+=b;
            }else{
                ti+=c/rate;
                break;
            }
        }
        printf("%.7lf\n",ti);
    }
    return 0;
}
