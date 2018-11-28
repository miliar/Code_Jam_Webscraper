#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int t;
    double fm,c,tt,t0,t2,f,x;
    cin>>t;
    for (int i=0; i<t; i++)
    {

            fm=2;
            t0=0;
            cin>>c>>f>>x;
        do
        {

            tt=x/fm+t0;

            t0=c/fm+t0;
            fm=fm+f;
            t2=x/fm+t0;
        }
        while (tt>t2);
            cout<<"Case #"<<i+1<<": "<<  fixed << setprecision( 7 ) <<tt<<endl;

    }
    return 0;
}
