#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>

using namespace std;

int main()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    double v,t,x,C,F,X;

    cin>>T;

    for(int i=0; i<T; i++)
    {
        cin>>C>>F>>X;
        x=0;
        t=0;
        v=2;

        while(x<X)
        {
            if(X-x <= C)
            {
                t+=(X-x)/v;
                x+=X-x;
            }
            else
            {
                t+=(C/v);
                x+=C;
                if((X-x)/v > (X)/(v+F))
                {
                    x-=C;
                    v+=F;
                }
                else
                {
                    t+=(X-x)/v;
                    x=X;
                }
            }

        }



        cout << "Case #" << i+1 << ": ";
        printf("%.7lf", t);
        cout << "\n";
    }

    return 0;
}

