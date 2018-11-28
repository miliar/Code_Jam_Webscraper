// OminousOmino.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

struct XRC
{
    int X = -1;
    int R = -1;
    int C = -1;
};

class InputReader
{
    int numCase_;
    std::ifstream file_;
public:
    InputReader(const string& fname) : file_("D:\\Miaso\\GoogleCodeJam\\input\\" + fname)
    {
        file_ >> numCase_;
    }

    XRC getNextCase()
    {
        XRC nextCase;
        if (numCase_ <= 0)
            return nextCase;

        file_ >> nextCase.X >> nextCase.R >> nextCase.C;
        numCase_--;

        return nextCase;
    }
};

int _tmain(int argc, _TCHAR* argv[])
{
    InputReader inputReader(".\\input_OminousOmino.txt");
    int noCase = 1;
    while (true)
    {
        const XRC nextCase = inputReader.getNextCase();
        if (nextCase.X==-1)
            break;
        int X = nextCase.X, R = nextCase.R, C = nextCase.C;
        bool bRichard = false;
        if (R*C%X != 0)
            bRichard = true;
        if (X > R && X > C)
            bRichard = true;
        int maxrc = std::max(R, C), minrc = std::min(R, C);
        if (X>2 && (X - minrc + 1) > minrc)
            bRichard = true;
        std::cout << "Case #" << noCase << ": ";
        cout << (bRichard ? "RICHARD" : "GABRIEL") << endl;
        noCase++;
    }

    return 0;
}

