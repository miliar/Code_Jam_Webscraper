#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>

class Tab
{
public:
    Tab();
    ~Tab();
    void arrange();
    std::vector<int> getRow(int row);
private:
    int t[4][4];
};

Tab::Tab()
{
}

Tab::~Tab()
{
}

void Tab::arrange()
{
    int i;
    int j;
    for (i = 0; i < 4; ++i)
        for (j = 0; j < 4; ++j)
            std::cin >> t[i][j];
}

std::vector<int> Tab::getRow(int row)
{
    std::vector<int> out;
    for (int i = 0; i < 4; ++i)
         out.push_back (t[row - 1][i]);
    return out;
}

int compare(std::vector<int> a, std::vector<int> b)
{
    int out = 0;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (a[i] == b[j])
                ++out;
    return out;
}

int response(std::vector<int> a, std::vector<int> b)
{
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (a[i] == b[j])
                return a[i];
    return 0;
}

int main()
{
    int testCases;
    int row;
    std::vector<int> first, second;
    std::cin >> testCases;
    for (int i = 0; i < testCases; ++i)
    {
        Tab tab;
        std::cin >> row;
        tab.arrange();
        first = tab.getRow(row);
        std::cin >> row;
        tab.arrange();
        second = tab.getRow(row);
        if (compare(first, second) == 1)
            std::cout << "Case #" << i + 1 << ": " << response(first, second) << std::endl;
        else if (compare(first, second) > 1)
            std::cout << "Case #" << i + 1 << ": " << "Bad magician!" << std::endl;
        else
            std::cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << std::endl;
    }
}
