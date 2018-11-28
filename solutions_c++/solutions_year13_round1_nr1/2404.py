#include<iostream>
#include<cmath>

using namespace std;

int main()
{
    long long r,t,T,tt;

    cin >> T;

    for(tt=1;tt<=T;tt++)
    {
        cin >> r >> t;

        cout << "Case #" << tt << ": " << (long long)(( sqrt((2*r-1)*(2*r-1) + 8*t)+ 1-r-r)*0.25) << "\n";
    }


    return 0;
}
