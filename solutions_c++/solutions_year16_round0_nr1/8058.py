#include <iostream>
#include <sstream>
#include <fstream>
#include <set>

std::string convertToString(int iValue)
{
    std::stringstream ss;
    ss << iValue;
    return ss.str();
}

int main( int argc, char* argv)
{
    std::ifstream fin("A-large.in");
    std::ofstream fout("A-large.out");
    int numTest;
    fin >> numTest;

    for(int testNum = 1; testNum <= numTest; testNum++)
    {
        int N;
        fin >> N;

        if(N == 0)
        {
            fout << "Case #" << testNum << ": INSOMNIA" << std::endl;
            continue;
        }

        std::set<int> numbersSet;
        bool sleeping = false;
        for(int i = 1; sleeping == false; i++)
        {
            int numToTest = i * N;
            std::string strNumToTest = convertToString(numToTest);

            for (int index = 0; index < strNumToTest.length(); index++)
            {
                numbersSet.insert(strNumToTest[index]);
            }

            if(numbersSet.size() == 10)
            {
                fout << "Case #" << testNum << ": " << numToTest << std::endl;
                sleeping = true;
            }

        }
    }

    fin.close();
    fout.close();
    return 0;
}

