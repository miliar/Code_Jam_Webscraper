#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

#include <boost/lexical_cast.hpp>
#include <boost/assign.hpp>

using namespace std;
using namespace boost;
using namespace boost::assign;


bool isFair(int number)
{
    vector<int> digits;
    while (number > 0)
    {
        digits.push_back(number % 10);
        number = number / 10;
    }
    for (int i=0; i < digits.size()/2; ++i)
    {
        if (digits[i] != digits[digits.size()-1-i])
            return false;
    }
    return true;
}

int main(int argc, char** argv)
{
    auto& in = cin;
    auto& out = cout;

    out << setprecision(7);

    string line;
    getline(in, line);
    int nLines = boost::lexical_cast<int>(line); 


    for (int caseNo=0; caseNo < nLines; ++caseNo)
    {
        out << "Case #" << caseNo+1 << ": ";
        
        int start, end;
        in >> start >> end;
       
        int sqStart = int(ceil(sqrt(start)));
        int sqEnd = int(floor(sqrt(end)));

        int nFair = 0;

        for (int i=sqStart; i <= sqEnd; ++i)
        {
            if (isFair(i) && isFair(i*i))
            {
                nFair++;
            }
        }

        out << nFair;
        out << endl;
    }


    return 0;
}

