#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
int ch[66];
int main()
{
    int t, c, d, v, nr[35];
    ifstream f("input.txt");
    ofstream g("output.txt");
    f>>t;
    int x;
    for (int i = 1; i <= t; i++)
    {
        f>>c>>d>>v;
        int ans = 0;
        memset(ch, 0, sizeof(ch));
        for (int j = 1; j <= d; j++)
        {
            f>>x;
            ch[x] = 1;
            nr[j] = x;
        }
        for (int  j = 1; j <= d; j++)
            for (int k = v; k >=1 ; k--)
                if (k != nr[j] && ch[k])
                    ch[nr[j]+k] = 1;
        for (int j = 1; j <= v; j++)
            if (!ch[j])
        {
            ans++;
            ch[j] = 1;
            for (int k = v; k >= 1; k--)
                if (k!=j && ch[k])
                    ch[j+k] = 1;

        }
        g<<"Case #"<<i<<": "<<ans<<'\n';

    }
}
