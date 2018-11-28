#include<iostream>
#include<stdio.h>
#include<iomanip>
using namespace std;

int main()
{
    //freopen("B-large.txt","r",stdin);
    //freopen("B_large_output.txt","w",stdout);
    int T;
    cin>>T;
    double c,f,x;
    double cumTime, cumTimeWithTarget;
    double rate;
    for(int t=1;t<=T;t++)
    {
        cin>>c>>f>>x;
        rate = 2.0;
        cumTime=0;//c/(rate*1.0f);
        cumTimeWithTarget = x/(rate*1.0f);

        while(cumTimeWithTarget > cumTime + c/(rate*1.0f) + x/((rate+f)*1.0f))
        {
            //rate += f;
            cumTime += c/(rate*1.0f);
            rate += f;
            cumTimeWithTarget = cumTime + x/(rate*1.0f);
        }
        cout << fixed << showpoint << setprecision(7);
        cout<<"Case #"<<t<<": "<<cumTimeWithTarget<<endl;
    }
}
