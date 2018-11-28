#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

void Case()
{
    int count;
    std::string in;
    std::cin >> count;
    std::vector<char> charChain;
    std::vector<std::vector<int> > chainCount;
    int first = 1;
    int fengalWon = 0;
    for (int i = 0; i < count; ++i)
    {
        std::cin >> in;
        char previous = -1;
        int ccount = 0;
        std::vector<int> countChain;
        if (first)
        {
            first = 0;
            char previous = -1;
            for (char c : in)
            {
                if (previous == -1 || previous != c)
                {
                    charChain.push_back(c);
                }
                previous = c;
            }
        }
        std::vector<char>::iterator chainIt = charChain.begin();
        for(char c : in)
        {
            if (previous == -1 || previous == c)
            {
                if (c != *chainIt || chainIt == charChain.end())
                    fengalWon = 1;
                ++ccount;
            }
            else
            {
                countChain.push_back(ccount);
                ccount = 1;
                ++chainIt;
                if (c != *chainIt || chainIt == charChain.end())
                    fengalWon = 1;
            }
            previous = c;
        }
        countChain.push_back(ccount);
        chainCount.push_back(countChain);
        if (++chainIt != charChain.end())
            fengalWon = 1;
    }
    if (fengalWon)
    {
        std::cout << "Fegla Won";
        return;
    }
    // compute number of action required
    std::vector<int> meanCount(charChain.size(), 0);
    for (std::vector<int> ccount : chainCount)
    {
        assert(ccount.size() == charChain.size());
        for (int i = 0; i < charChain.size(); ++i)
        {
            assert(ccount[i] > 0);
            meanCount[i] += ccount[i];
        }
    }
    for (int i = 0; i < charChain.size(); ++i)
    {
        meanCount[i] /= chainCount.size();
    }

    int actionCount = 0;
    for (std::vector<int> ccount : chainCount)
        for (int i = 0; i < charChain.size(); ++i)
        {
            actionCount += std::abs(ccount[i] - meanCount[i]);
        }
    std::cout << actionCount;
}

int main()
{
    int caseCount = 0;

    std::cin >> caseCount;
    for (int i = 1; i <= caseCount; ++i)
    {
        std::cout << "Case #" << i << ": ";
        Case();
        std::cout << std::endl;
    }
}
