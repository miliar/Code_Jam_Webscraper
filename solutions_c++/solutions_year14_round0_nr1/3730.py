#include <algorithm>
#include <iostream>
#include <vector>
#include <list>

void Case(int i)
{
    int choice1, choice2;
    std::vector<int> row1(4), row2(4);
    std::cin >> choice1;
    --choice1;
    // skip
    for (int i = 0; i < choice1 * 4; ++i)
    {
        int dummy;
        std::cin >> dummy;
    }
    // fetch
    for (int i = 0; i < 4; ++i)
        std::cin >> row1[i];
    // skip
    for (int i = 0; i < (4-choice1-1) * 4; ++i)
    {
        int dummy;
        std::cin >> dummy;
    }
    std::cin >> choice2;
    --choice2;
    // skip
    for (int i = 0; i < choice2 * 4; ++i)
    {
        int dummy;
        std::cin >> dummy;
    }
    // fetch
    for (int i = 0; i < 4; ++i)
        std::cin >> row2[i];
    // skip
    for (int i = 0; i < (4-choice2-1) * 4; ++i)
    {
        int dummy;
        std::cin >> dummy;
    }

    std::list<int> answer;
    for (int i = 0; i < 4; ++i)
    {
        std::vector<int>::iterator found = std::find(row2.begin(), row2.end(), row1[i]);
        if (found != row2.end())
            answer.push_back(row1[i]);
    }

    std::cout << "Case #" << i << ": ";
    switch(answer.size())
    {
    case 1:
        std::cout << answer.front();
        break;
    case 0:
        std::cout << "Volunteer cheated!";
        break;
    default:
        std::cout << "Bad magician!";
    }
    std::cout << std::endl;
}

int main()
{
    int caseCount;

    std::cin >> caseCount;
    for (int i = 1; i <= caseCount; ++i)
        Case(i);
    return 0;
}
