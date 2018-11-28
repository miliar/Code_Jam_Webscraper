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
    for(int i = 1; i <= t; i++)
    {
        string s;
        f >> s;

        bool ok = true;
        int ans = 0;
        while(ok)
        {
            ok = false;
            int poz = -1;
            for(int j = s.size() - 1; j >= 0 && poz == -1; j--)
                if(s[j] == '-')
                    poz = j;

            if(poz != -1)
                {
                    ans ++;
                    ok = true;
                }

            for(int j = poz; j >= 0; j--)
                if(s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';

        }
        g << "Case #"<<i<<": "<<ans<<'\n';
    }


    return 0;
}
