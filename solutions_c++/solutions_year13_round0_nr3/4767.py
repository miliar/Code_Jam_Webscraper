#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <math.h>

bool isPalindrome( long num )
{
    std::string strNum;
    std::stringstream stream;

    stream << num;
    stream >> strNum;

    //std::cout << "Testing " << strNum << std::endl;
    if (strNum.size() == 1)
    {
        return true;
    }

    int start = 0;
    int end = strNum.size() - 1;

    while (start < end)
    {
        if (strNum[start++] != strNum[end--])
        {
            return false;
        }
    }

    return true;
}

bool isSquareRootPalindrome( long num )
{
    float root = sqrt(num);

    //std::cout << "Second : " << root << " " << fmod(root,1.0f) << " " << (long)root << std::endl;
    if ((fmod(root,1.0f) == 0) && isPalindrome((long)root))
    {
        return true;
    }

    return false;
}

int main ( void )
{
    std::ifstream file;

    file.open("fair-small.in");

    int numTestCases = 0;

    file >> numTestCases;
    //std::cout << "numTestCases " << numTestCases << std::endl;

    for(int i = 1; i <= numTestCases; i++)
    {
        long start;
        long end;
        int count = 0;

        file >> start;
        file >> end;

        for (long j = start; j <= end; j++)
        {
            if (isPalindrome(j) && isSquareRootPalindrome(j))
            {
                //std::cout << "Found : " << j << std::endl;
                count++;
            }
        }

        std::cout << "Case #" << i << ": " << count << std::endl;
    }

    return 0;
}

