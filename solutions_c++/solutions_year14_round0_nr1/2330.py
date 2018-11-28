#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int cases;
    std::cin >> cases;
    
    for (int casenum = 1; casenum <= cases; ++casenum)
    {
        std::vector<int> rows[2];
        for (int i = 0; i < 2; ++i)
        {
            int whichRow;
            std::cin >> whichRow;
            
            for (int k = 0; k < 16; ++k)
            {
                int card;
                std::cin >> card;
                
                int thisRow = k / 4 + 1;
                if (thisRow == whichRow)
                {
                    rows[i].push_back(card);
                }
            }

            std::sort(rows[i].begin(), rows[i].end());
        }

        std::vector<int> matches(4);
        // for (int i = 0; i < 2; ++i)
        // {
        //     std::for_each(rows[i].begin(), rows[i].end(), [](int v){std::cout << v << " ";});
        //     std::cout << std::endl;
        // }
        std::set_intersection(rows[0].begin(), rows[0].end(), rows[1].begin(), rows[1].end(), matches.begin());
        // std::for_each(matches.begin(), matches.end(), [](int v){std::cout << v << " ";});
        // std::cout << std::endl;

        std::cout << "Case #" << casenum << ": ";
        if (matches[0] && matches[1])
        {
            std::cout << "Bad magician!\n";
        }
        else if (matches[0])
        {
            std::cout << matches[0] << std::endl;
        }
        else
        {
            std::cout << "Volunteer cheated!\n";
        }
    }
    return 0;
}
