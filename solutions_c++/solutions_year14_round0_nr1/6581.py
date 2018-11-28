#include <iostream>
#include <unordered_set>
#include <algorithm>


int main(int argc, char *argv[])
{
    int t;
    std::cin >> t;
    for (int testcase=0; testcase < t; ++testcase)
    {
        int ans1;
        std::cin >> ans1;
        --ans1;
        std::unordered_set<int> roi1;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                int item;
                std::cin >> item;
                if (i == ans1)
                {
                    roi1.insert(item);
                }
            }
        }

        int ans2;
        std::cin >> ans2;
        --ans2;
        std::unordered_set<int> roi2;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                int item;
                std::cin >> item;
                if (i == ans2)
                {
                    roi2.insert(item);
                }
            }
        }

        std::vector<int> isec(4);
        int ctr = 0;
        auto begin = roi2.begin(),
             end = roi2.end();
        for (auto it = roi1.begin(); it != roi1.end(); ++it)
        {
            if (std::find(begin, end, *it) != end)
            {
                isec[ctr++] = *it;
            }
        }
        std::cout << "Case #" << testcase + 1 << ": ";
        switch (ctr)
        {
        case 1:
            std::cout << *isec.begin();
            break;
        case 0:
            std::cout << "Volunteer cheated!";
            break;
        default:
            std::cout << "Bad magician!";
        }
        std::cout << std::endl;
    }
    return 0;
}
        

