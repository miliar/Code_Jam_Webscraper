// CodeJam2016-2.cpp : Defines the entry point for the console application.
//


#include <fstream>
#include <sstream>
#include <string>
#include <bitset>

int cake(std::string input)
{
    auto isUp = [&](int k)
    {
        return input.at(k) == '+';
    };

    bool firstUp = isUp(0);
    int flip = 0;
    bool lastUp = firstUp;
    for (int i = 1; i < input.size(); i++)
    {
        bool currentUp = isUp(i);
        if (currentUp != lastUp)
        {
            flip++;
            lastUp = currentUp;
        }
    }

    if (!lastUp)
    {
        flip++;
    }

    return flip;
}

int main()
{
    std::ifstream input("2.in");

    int cases = 0;
    input >> cases;
    std::string line;
    std::getline(input, line);
    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        std::getline(input, line);

        printf("Case #%d: %d\n", caseNumber + 1, cake(line));
    }

    getchar();

    return 0;
}

