#include<iostream>
#include <iomanip>
using namespace std;



int main()
{
    int T;
    double C,X,F;
    int i,j,k;
    cin>>T;
    double noc=0;double rate=2.0;
    double t=0;
    double time[T];

    for(i=0;i<T;i++)
    {
        cin>>C>>F>>X;
    noc=0;t=0;rate=2;
    do
    {
        if(C<X)
        {
        noc+=C;
        t+=C/rate;
        //cout<<"reached1: "<<t;// cout<<" :"<<X/rate<<" :"<<(C/rate)+X/(rate+F);
        if((X/rate) > ((C/rate)+X/(rate+F)))
        {
            noc=0;
            rate+=F;

        }
        else
        {
            t+=(X-noc)/rate;
            noc=X;
        }

        }
        else
            {
                noc=X;
                t=X/rate;
            }

    }while(noc!=X);
        time[i]=t;
    }
    for(i=0;i<T;i++)
    {
        cout<<"\nCase #"<<i+1<<": ";
        std::cout << std::fixed << std::setprecision(7) <<time[i];

    }
}
