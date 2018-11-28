#include <iostream>
#include <fstream>
#include <queue>
#include <set>
using namespace std;

ifstream f("data.in");
ofstream g("data.out");

int main()
{
    int t;
    f >> t;
    unsigned long long a,b,c;
    for(int i = 1; i <= t; i++)
    {
        f >> a;
        b = a;

        if(a == 0)
            g <<"Case #"<<i<<": "<<"INSOMNIA\n";
        else
        {
            int f[10] = {0};
            bool ok = false;

            c = a;
            while(c)
                {
                    f[c%10] = 1;
                    c /= 10;
                }

            while(!ok)
            {
                    b += a;
                    c = b;
                    while(c)
                    {
                        f[c%10] = 1;
                        c /= 10;
                    }

                ok = true;
                for(int i = 0; i <= 9; i++)
                    if(f[i] == 0)
                        ok = false;


            }

            g <<"Case #"<<i<<": "<< b << '\n';
        }
    }

    return 0;
}
