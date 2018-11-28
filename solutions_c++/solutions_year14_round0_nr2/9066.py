#include <iostream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main()
{
    int a;
    long double c,f,x,d,t=0.0000000;
    freopen("input.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    cin>>a;

    for(int i=0;i<a;i++){
    cin>>c>>f>>x;
    d=2.0000000;
    t=0.0000000;
    while((x/d)>((x/(d+f))+(c/d)))
    {

        t=t+(c/d);
        d=d+f;
    }
    t=t+(x/d);
    cout<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<t<<endl;
    }
    return 0;
}
