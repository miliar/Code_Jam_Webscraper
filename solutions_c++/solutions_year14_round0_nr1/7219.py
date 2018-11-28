#include <iostream>
#include <vector>

int main(int argc, const char * argv[])
{
    freopen("/Users/yuristuken/Documents/codejam14/A/A/A-small-attempt0.in", "r", stdin);
    freopen("/Users/yuristuken/Documents/codejam14/A/A/A-small-attempt0.out", "w", stdout);
    int nTests;
    std::cin >> nTests;
    for (int test = 1; test <= nTests; ++test)
    {
        std::vector<size_t> firstRow(4), secondRow(4);
        size_t firstRowNumber, secondRowNumber;
        std::cin >> firstRowNumber;
        
        for (size_t currentRow = 1; currentRow <= 4; ++currentRow)
        {
            
            if (currentRow != firstRowNumber)
            {
                size_t null;
                std::cin >> null >> null >> null >> null;
                continue;
            }
            
            for (size_t currentCol = 0; currentCol < 4; ++currentCol)
            {
                std::cin >> firstRow.at(currentCol);
            }
        }
        
        std::cin >> secondRowNumber;
        
        for (size_t currentRow = 1; currentRow <= 4; ++currentRow)
        {
            if (currentRow != secondRowNumber)
            {
                size_t null;
                std::cin >> null >> null >> null >> null;
                continue;
            }
            for (size_t currentCol = 0; currentCol < 4; ++currentCol)
            {
                std::cin >> secondRow.at(currentCol);
            }
        }
        
        std::sort(firstRow.begin(), firstRow.end());
        std::sort(secondRow.begin(), secondRow.end());
        
        std::vector<size_t> intersection;
        
        std::set_intersection(firstRow.begin(), firstRow.end(),
                              secondRow.begin(), secondRow.end(), std::back_inserter(intersection));
        
        std::cout << "Case #" << test << ": ";
        if (intersection.size() == 0)
        {
            std::cout << "Volunteer cheated!";
        }
        else if (intersection.size() == 1)
        {
            std::cout << intersection.front();
        }
        else
        {
            std::cout << "Bad magician!";
        }
        std::cout << std::endl;
    }
    return 0;
}

