#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdio.h>
#define lfo(i,a,b) for (int i=a,_b=b ; i<=_b ; ++i)

using namespace std;
int t;
double c,x,f;

void Solve(int k)
{
    double tg=2;
    double t=0;
    while (true)
    {
        if (x/tg<=c/tg)
        {
            t=t+x/tg;
            break;
        }
        else
        {
            if (x/(tg+f)<=(x-c)/tg)
            {
                t=t+c/tg;
                tg=tg+f;
            }
            else
            {
                t=t+x/tg;
                break;
            }
        }
    }
    cout<<"Case #"<<k<<": ";
    printf("%0.7f\n",t);
}

int main()
{
    freopen("","r",stdin);
    freopen("","w",stdout);
    cin>>t;
    lfo(k,1,t)
    {
        cin>>c>>f>>x;
        Solve(k);
    }
    return 0;
}
