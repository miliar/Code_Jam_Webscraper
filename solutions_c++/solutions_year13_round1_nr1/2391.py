#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;


int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,TT;
    int i,j,k,n,m;
    long long r,t,y;
    long double temp;


    cin>>T;TT=1;
    while (T--)
    {
        cin>>r>>t;
        temp=pow((long double)((2*r-1)*(2*r-1)+8*t),0.5);
        y=(1-2*r+temp)/4;


        cout<<"Case #"<<TT<<": "<<y<<endl;

        TT++;
    }

    return 0;
}
