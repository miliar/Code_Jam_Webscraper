#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int main()
{   READ("B-large.in");
    WRITE("B-Small.out");
    long int t;
    double c,f,x;
    double S,R,T;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        cin>>c>>f>>x;
        R=2.000;
        T=0.0000;
        S = ((c-x)/R)+(x/(R+f));
        while(S<0.0000000)
        {
            T = T + (c/R);
            R+=f;
            S = ((c-x)/R)+(x/(R+f));
        }
        T= T + (x/R);
        printf("Case #%d: %.7lf\n",k,T);

    }
    return 0;
}
