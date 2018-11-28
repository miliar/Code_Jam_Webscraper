#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

double eps = 1e-8;
inline int sig(double x)
{
    if(x > eps) return 1;
    else if(x < -eps) return -1;
    else return 0;
}


int main()
{
    int T;
    cin >> T;

    for(int c=0; c<T; c++)
    {
        double C, F, X;
        cin >> C >> F >> X;

        double t = 0.0, cps = 2.0;
        while(true)
        {
            double tf1 = X / cps;
            double tf2 = X / (cps + F) + C / cps;
            
            if(sig(tf1 - tf2) < 0)
            {
                t += tf1;
                break;
            }   
            else
            {
                t += C / cps;
                cps += F;
            }
        }

        printf("Case #%d: %.7lf\n", c+1, t);
    }

    return 0;
}
