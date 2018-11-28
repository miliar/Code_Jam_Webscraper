// CodeJam2016-2.cpp : Defines the entry point for the console application.
//

#include <stdint.h>
#include <fstream>
#include <sstream>
#include <string>
#include <bitset>
#include <vector>

#define DB true

void word(std::string input)
{
    std::string result = "";
    result += input[0];

    for (int i = 1; i < input.size(); i++)
    {
        std::string before = input[i] + result; 
        std::string after = result + input[i];

        if (before > after)
        {
            result = before;
        }
        else
        {
            result = after;
        }
    }

    printf("%s\n", result.c_str());
}

int main()
{
    std::ifstream input("1.in");

    int cases = 0;
    input >> cases;

    std::string line;
    std::getline(input, line);

    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        printf("Case #%d: ", caseNumber + 1);

        std::getline(input, line);

        word(line);
    }

    DB && getchar();

    return 0;
}

