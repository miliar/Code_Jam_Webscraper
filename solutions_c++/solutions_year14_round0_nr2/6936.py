#include <cstdio>
#include <iostream>
#include <float.h>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int p, o;
    cin>>o;
    p=o;
    while(o--){
        double c, f, x, t=0;
        cin>>c>>f>>x;
        int k = ( (f*x -2*c)/(f*c) );
        double i;
        for(i=0; i<k; ++i){
            t+=c/(i*f+2);
        }
        t+=x/(i*f+2);
        cout<<"Case #"<<p-o<<": ";
        printf("%.7f\n", t);
    }
    return 0;
}
