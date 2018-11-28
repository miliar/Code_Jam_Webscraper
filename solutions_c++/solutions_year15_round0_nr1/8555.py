#include <cstdio>
#include <stdlib.h>
#include <string>
#include <iostream>

int main()
{
    std::ios_base::sync_with_stdio(0);

    int T = 0, S = 0;
    int members = 0, minFriends = 0;
    std::string tab = "";

    std::cin >> T;

    for(int i = 1; T--; ++i)
    {
        members = minFriends = 0;
        std::cin >> S >> tab;

        if(tab.size() <= 1)
        {
            std::cout << "Case #" << i << ": 0\n";
            continue;
        }

        for(int a = 0; a < tab.size(); ++a)
        {
            if(a > members && int(tab[a]-'0') > 0)
            {
                minFriends += (a - members);
                members += (a - members);
            }

            members += int(tab[a] - '0');
        }


        std::cout << "Case #" << i << ": " << minFriends << "\n";
    }

    return 0;
}
