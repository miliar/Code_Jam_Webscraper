#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    double  c, f, x, p = 2, tiempo = 0;

    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> c >> f >> x;

        while(true)
        {
            if((x/p) < ((x/(p+f))+(c/p)))
            {
                tiempo += x/p;
                break;
            }
            tiempo += c/p;
            p += f;
        }

        printf("Case #%d: %.7f\n", i+1, tiempo);
        p = 2;
        tiempo = 0;
    }

    return 0;
}
