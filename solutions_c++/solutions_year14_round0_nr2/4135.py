#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int q=1;q<=t;q++)
    {
        double c,f,x;
        cin >> c >> f >>x;
        printf("Case #%d: ",q);
        double t=0;
        double e=0;
        while(x/(2+e)> c/(2+e) + x/(2+e+f) )
        {
            t+=c/(2+e);
            e+=f;
        }
        t+=x/(2+e);
        printf("%.7f\n",t);
    }
    return 0;
}
