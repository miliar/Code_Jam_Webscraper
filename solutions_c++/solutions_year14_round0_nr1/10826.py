#include <iostream>
#include <set>
#include <vector>

int main()
{
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++)
    {
        int guess1, guess2;
        int arr1[4][4];
        int arr2[4][4];

        std::cin >> guess1;
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                std::cin >> arr1[j][k];
            }
        }

        std::cin >> guess2;
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                std::cin >> arr2[j][k];
            }
        }

        int *row1 = arr1[guess1 - 1];
        int *row2 = arr2[guess2 - 1];

        std::set<int> set1(row1, row1 + sizeof(row1));

        std::cout << "Case #" << i + 1 << ": ";

        std::vector<int> matches;

        for (int i = 0; i < 4; i++)
        {
            if (set1.find(row2[i]) != set1.end())
                matches.push_back(row2[i]);
        }

        if (matches.size() == 1)
        {
            std::cout << matches[0] << std::endl;
        }
        else if (matches.size() > 1)
        {
            std::cout << "Bad magician!" << std::endl;
        }
        else
        {
            std::cout << "Volunteer cheated!" << std::endl;
        }

    }
}
