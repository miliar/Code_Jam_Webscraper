#include <iostream>
#include <cmath>
#include <cstdio>
#include <assert.h>
#include <algorithm>

using namespace std;

string s;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    freopen("A-large.in" , "r" , stdin);
    freopen("out.out" , "w" , stdout);

    int T , cc = 0;
    cin >> T;
    while(T--)
    {
        ++cc;
        cin >> s;
        int last = s.size() - 1;

        int st = 0 , en = s.size() - 1;
        string output;
        output.resize(s.size());

        while(1)
        {
            int idx = -1;
            bool done  = false;
            for(int i = 'Z';i >= 'A' and !done;--i)
            {
                for(int j = last;j > -1 and !done;--j)
                {
                    if(s[j] == i)
                    {
                        idx = j;
                        done = true;
                    }
                }
            }
            output[st++] = s[idx];
            for(int i = last;i > idx;--i)
                output[en--] = s[i];

            last = idx - 1;
            if(en < st)        break;
        }
        cerr << cc << "   ->   done    " << output.size() << "\n";
        cout << "Case #" << cc << ": " << output << "\n";
    }
    return 0;
}
