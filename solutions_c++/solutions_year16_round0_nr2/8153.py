#include <iostream>
#include <fstream>

int findSignChangePos(std::string iValue)
{
    int pos = -1;
    char temp = iValue[0];
    for(size_t index = 1; index < iValue.length(); index++)
    {
        if(temp != iValue[index])
        {
            pos = index;
            break;
        }
    }
    return pos;
}

std::string reverseSign(std::string iValue, int pos)
{
    char c = iValue[pos - 1];
    if(c == '+')
    {
        iValue.replace(0, pos, pos, '-');
    }
    else
    {
        iValue.replace(0, pos, pos, '+');
    }
    return iValue;
}
int main()
{
    std::ifstream fin("B-large.in");
    std::ofstream fout("B-large.out");

    int numTest = 0;
    fin >> numTest;

    for(int testNum = 0; testNum < numTest; testNum++)
    {
        std::string testString;
        fin >> testString;

        //std::string testString(temp);

        int pos = findSignChangePos(testString);
        int flipCount = 0;
        while(pos != -1)
        {
            testString = reverseSign(testString, pos);
            pos = findSignChangePos(testString);
            flipCount++;
        }

        flipCount = (testString[0] == '-') ?  flipCount + 1 : flipCount;

        fout << "Case #" << testNum + 1 << ": " << flipCount << std::endl;
    }

    fin.close();
    fout.close();
}
