#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define in cin
#define out cout
#define REP(i,s,e) for(int i=s; i<=e; i++)

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tc; in >> tc;
    for(int tci=1; tci<=tc; tci++)
    {
        int n; in >> n;
        string str; in >> str;

        int res = 0;
        int ppl = str[0]-'0';
        for(int i=1; i<=n; i++)
        {
            if(i > ppl)
            {
                res += i-ppl;
                ppl += i-ppl;
            }

            ppl += str[i]-'0';
        }

        out << "Case #" << tci << ": " << res << endl;
    }


    return 0;
}
