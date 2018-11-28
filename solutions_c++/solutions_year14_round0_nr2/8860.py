#include<iostream>
#include <iomanip>

using namespace std;

int main()
{
    double c, x, f, cur=0.0, time = 0.0, rate = 2.0;
    int i,t;
    cin>>t;
    for ( i = 0 ; i < t ; ++i )
    {
        cin>>c>>f>>x;
        while ( 1 )
        {
            if ( x/rate > ( ( c / rate ) + ( x / ( rate + f ) ) ) )
            {
                time += c/rate;
                rate += f;
            }
            else
            {
                time += x/rate;
                break;
            }
        }
        cout<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<time<<endl;
        time = 0;
        rate = 2;
        cur = 0;
    }
}


