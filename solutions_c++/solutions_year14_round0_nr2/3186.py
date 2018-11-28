#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

//#define MY_TEST

int main()
{
    #ifndef MY_TEST
    freopen("input.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    #endif // MY_TEST

    int T,k;
    long double C,F,X,ck,pr,t;

    cin>>T;
    for(k=1;k<=T;++k)
    {
        cin>>C>>F>>X;
        ck=0;
        pr=2.0;     //Production rate
        t=0.0;  //time
        while(ck!=X)
        {
            if(((X/(pr+F))+ (C/pr))<(X/pr))
            {
                t += C/pr;
                pr += F;
                ck=0.0;
                continue;
            }
            t += X/pr;
            ck = X;
        }
        cout<<"case #"<<k<<": "<<setprecision(7)<<fixed<<t<<endl;
    }

    return 0;
}
