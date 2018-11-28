// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <vector>
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

    std::string getNextCase()
    {
        std::string nextCase;
        if (numCase_ <= 0)
            return nextCase;

        int l, x;
        file_ >> l >> x;
        string str;
        file_ >> str;
        nextCase.reserve(x*l);
        for (int i = 0; i < x; i++)
            nextCase.append(str);

        numCase_--;
        return nextCase;
    }
};

const char minus1 = static_cast<char>('1'*-1);
const char minusk = static_cast<char>('k'*-1);
const char minusj = static_cast<char>('j'*-1);
const char minusi = static_cast<char>('i'*-1);

inline int getRowNo(char c)
{
    switch (c)
    {
    case '1':
    case minus1:
        return 0;
    case 'i':
    case minusi:
        return 1;
    case 'j':
    case minusj:
        return 2;
    case 'k':
    case minusk:
        return 3;
    }

    throw "unexpected";
}

char merge(char ch1, char ch2)
{
    const int multiplier = ((ch1 < 0 && ch2 < 0) || (ch1>0 && ch2>0) ? 1 : -1);
    static std::vector <std::vector<int > > data = {
        { '1', 'i', 'j', 'k' },
        { 'i',  minus1, 'k', minusj },
        { 'j', minusk, minus1, 'i' },
        { 'k', 'j', minusi, minus1 }
    };
    char ch = data[getRowNo(ch1)][getRowNo(ch2)];

    return static_cast<char>(ch*multiplier);
}

class StrParser
{
    int kpos_ = -2;
    const std::string& str_;
public:
    StrParser(std::string& str) : str_(str) { }
    int getNextKPos();
    std::vector<int> getAllIPos();
    char evaluate(int pos1, int pos2);
};

int StrParser::getNextKPos()
{
    if (kpos_ == -1)
        return -1;

    char lastchar = 'k';
    if (kpos_ == -2)
    {
        lastchar = str_.back();
        kpos_ = str_.size() - 1;
        if (lastchar == 'k')
            return kpos_;
    }

    while (true)
    {
        kpos_--;
        if (kpos_ < 0)
            break;
        lastchar = merge(str_[kpos_], lastchar);
        if (lastchar == 'k')
            break;
    }

    return kpos_;
}

std::vector<int> StrParser::getAllIPos()
{
    std::vector<int> vecIpos;

    char firstChar = str_[0];
    if (firstChar == 'i')
        vecIpos.push_back(0);
    for (int i = 1; i < str_.size(); i++)
    {
        firstChar = merge(firstChar, str_[i]);
        if (firstChar == 'i')
            vecIpos.push_back(i);
    }

    return vecIpos;
}

char StrParser::evaluate(int pos1, int pos2)
{
    char ch = str_[pos1 + 1];
    for (int i = pos1 + 2; i < pos2; i++)
        ch = merge(ch, str_[i]);
    return ch;
}

int _tmain(int argc, _TCHAR* argv[])
{
    InputReader inputReader(".\\input_Dejkstra.txt");
    int noCase = 1;
    while (true)
    {
        std::string nextCase = inputReader.getNextCase();
        if (nextCase.empty())
            break;

        bool bFound = false;
        StrParser parser(nextCase);
        std::vector<int> vecIpos = parser.getAllIPos();
        int kpos = parser.getNextKPos();
        while (kpos > 0 && !bFound)
        {
            char lastResult = '0';
            int lastipos = -1;
            int newsize = vecIpos.size();
            for (std::vector<int>::reverse_iterator rit = vecIpos.rbegin(); rit != vecIpos.rend(); rit++)
            {
                int ipos = *rit;
                if (ipos >= (kpos-1))
                {
                    newsize--;
                    continue;
                }
                char result = '0';
                if (lastipos > 0)
                {
                    result = merge(parser.evaluate(ipos, lastipos), lastResult);
                }
                else
                    result = parser.evaluate(ipos, kpos);
                if (result == 'j')
                {
                    bFound = true;
                    break;
                }
                lastResult = result;
                lastipos = ipos + 1;
            }
            vecIpos.resize(newsize);
            kpos = parser.getNextKPos();
        }

        std::cout << "Case #" << noCase << ": " << (bFound ? "YES" : "NO") << endl;
        noCase++;
    }

    return 0;
}

