// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <deque>
#include <iostream>

using namespace std;

class InputReader
{
    int numCase_;
    std::ifstream file_;
public:
    InputReader(const string& fname) : file_("D:\\Miaso\\GoogleCodeJam\\input\\" + fname)
    {
        file_ >> numCase_;
    }

    std::deque<int> getNextCase()
    {
        std::deque<int> nextCase;
        if (numCase_ <= 0)
            return nextCase;

        int smax;
        std::string sinfo;
        file_ >> smax >> sinfo;
        smax++;
        while (!sinfo.empty())
        {
            nextCase.push_front(sinfo.back() - '0');
            sinfo.resize(sinfo.size() - 1);
        }
        while (nextCase.size() < smax)
            nextCase.push_front(0);

        numCase_--;
        return nextCase;
    }
};

int _tmain(int argc, _TCHAR* argv[])
{
    InputReader inputReader(".\\input_StandingOvation.txt");
    int noCase = 1;
    while (true)
    {
        const std::deque<int>& nextCase = inputReader.getNextCase();
        if (nextCase.empty())
            break;
        std::cout << "Case #" << noCase <<": ";
        int numStanding = 0, numExtraTotal = 0;
        for (int i = 0; i < nextCase.size(); i++)
        {
            if (numStanding < i)
            {
                int numExtra = i - numStanding;
                numExtraTotal += numExtra;
                numStanding += numExtra;
            }
            numStanding += nextCase[i];
        }
        cout << numExtraTotal << endl;
        noCase++;
    }

    return 0;
}

