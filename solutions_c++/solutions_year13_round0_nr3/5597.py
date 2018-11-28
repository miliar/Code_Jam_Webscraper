#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
   freopen("the2sim.out", "w", stdout);
    int t , a, b;
    int w[1005] ;
    cin>>t;
    memset(w, 0, sizeof(w));

    w[0] = 0;

    for (int i = 1; i < 10; i++)
    {
        if(double(double(sqrt(double(i))) - int(sqrt(double(i))) )  > 0.0)
        {
            w[i] = w[i-1];
        }
        else
        {
            w[i] = w[i-1] + 1;
        }
    }

    for (int i = 10; i < 100; i++)
    {
        int tmp = i , gw = i;
        gw = i % 10;
        tmp /= 10;

        if(gw != tmp || double(double(sqrt(double(i))) - int(sqrt(double(i))) )  > 0.0)
        {
            w[i] = w[i-1];
        }
        else
        {
            w[i] = w[i-1] + 1;
        }
    }

    for (int i = 100; i < 1000; i++)
    {
        int tmp = i , gw = i;
        gw = i % 10;
        tmp /= 10;
        tmp /= 10;


        if(gw != tmp || double(double(sqrt(double(i))) - int(sqrt(double(i))) )  > 0.0)
        {
            w[i] = w[i-1];
        }
        else
        {
            int kk = int(sqrt(double(i)));
            gw = kk % 10;
            kk /= 10;

            if (kk == gw)
                w[i] = w[i-1] + 1;
            else w[i] = w[i-1];
        }
    }

    w[1000] = w[999];


    for (int tt = 1;  tt <= t; tt++ )
    {
        cout<<"Case #"<<tt<<": ";
        cin>>a>>b;

        if ( w[a] - w[a-1] > 0)
            cout<<w[b] - w[a] + 1<<endl;
        else
            cout<<w[b] - w[a]<<endl;

    }
    return 0;
}
