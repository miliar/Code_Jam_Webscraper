#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

int main()
{
    std::ifstream in("in");
    std::ofstream out("out");

    int T;
    in >> T;

    short sMax;
    std::string number;
    for(int caseNum = 1; caseNum <= T; ++caseNum)
    {
        out << "Case #" << caseNum << ": ";

        in >> sMax >> number;
        int standingPeople = 0;
        int neededPeople = 0;
        for(short i = 0; i < sMax+1; ++i)
        {
            short digit;
            digit = number[i] - '0';
            if(digit == 0 || standingPeople >= i)
            {
                standingPeople += digit;
            }
            else
            {
                neededPeople += i - standingPeople;
                standingPeople += neededPeople + digit;
            }
        }

        out << neededPeople << '\n';
    }

    return 0;
}

