#include <string>
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int t;

    std::cin >> t;

    for(int it = 0; it < t; it++)
    {
        int s_max;
        cin >> s_max;

        string s;

        cin >> s;

        int total = 0;
        int answer = 0;
        for(int ix = 0; ix < s.size(); ix++)
        {
            int dd = s[ix] - '0';

            if(total < ix)
            {
                answer += (ix - total);
                total = ix;
            }


            total += dd;
        }

        printf("Case #%d: %d\n", it + 1, answer);
    }
    return 0;
}
