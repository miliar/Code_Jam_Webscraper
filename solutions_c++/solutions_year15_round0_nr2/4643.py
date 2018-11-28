#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream f("p.in");
    ofstream g("p.out");
    int T, i, j, D, p[1001], val, ans, maxval = 0, maxans;
    f>>T;
    for (i = 1; i <= T; i++)
    {
        f>>D;
        for (j = 0; j < D; j++) {f>>p[j]; if (p[j]>maxval) maxval = p[j];}
        maxans = 1001;
        ans = 0;
        for (val = 1; val <= maxval; val++)
            {
                ans = 0;
                for (j = 0; j < D; j++)
                if (p[j]>val) ans+=p[j]/val - !(p[j]%val);
            if (ans+val<maxans) maxans = ans + val;}
        g<<"Case #"<<i<<": "<<maxans<<'\n';
    }
}
