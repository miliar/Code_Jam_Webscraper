#include <iostream>
#include <iomanip>
#include <cmath>
#define N 1000
using namespace std;

int main()
{
    int n,i=0;
    cin>>n;
    while (i<n){
        double c,f,x;
        cin>>c>>f>>x;

        double t1,t2,tf,tmin,ll;
        int j=0;
        t1=0;
        tmin=10e10;
        while (j<10000000) {
            ll=(f*j+2);

            tf=t1+x/ll;
            if (tmin>tf) {tmin=tf;}
            t1+=c/ll;
            j++;
        }
        cout<<fixed;
        cout<<setprecision(7);
        cout<<"Case #"<<i+1<<": "<<tmin<<endl;
        i++;
    }
    return 0;
}

