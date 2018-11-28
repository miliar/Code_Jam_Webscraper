#include <bits/stdc++.h>

int main (int argc, char *argv[])
{
    std::ifstream inputStream("E:\\A-large.in");
    std::ofstream outputStream("E:\\ccouta.txt");
    std::size_t numOfTestCases = 0;
    inputStream >> numOfTestCases;

    for (std::size_t ix = 0; ix < numOfTestCases; ++ix)
    {
        std::size_t numOfShynessLevels = 0;
        inputStream >> numOfShynessLevels;

        std::string shyPeople;
        inputStream >> shyPeople;
        int totalPoints = 0;
        int shynessGroup = 0;
        int answer = 0;

        for (auto val: shyPeople)
        {
            int integerVal = val - '0';
            if (totalPoints < shynessGroup)
            {
                answer += (shynessGroup - totalPoints);
                totalPoints = shynessGroup;
            }
            totalPoints += integerVal;
            ++shynessGroup;
        }

        outputStream << "Case #" << ix + 1 << ": ";
        outputStream << answer << "\n";
    }

    inputStream.close();
    outputStream.close();
}
