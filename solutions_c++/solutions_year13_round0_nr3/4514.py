#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
#include <set>

// Usage:
// cat input.txt | ./main > output.txt
// ./main input.txt > output.txt
// ./main input.txt output.txt

void processAllCases(std::istream &is, std::ostream &os);
void processCase(const int caseNumber, std::istream &is, std::ostream &os, const std::set<long long> &preCalculatedFairAndSquare);

int main(int argc, char *argv[]) {
    std::ostream* os;
    std::istream* is;
    std::ofstream fout;
    std::ifstream fin;
    switch(argc) {
        case 1:
            os = &std::cout;
            is = &std::cin;
            break;
        case 2:
            fin.open(argv[1]);
            is = &fin;
            os = &std::cout;
            break;
        case 3:
            fin.open(argv[1]);
            is = &fin;
            fout.open(argv[2]);
            os = &fout;
            break;
        default:
            std::cout
                << "Usage:" << std::endl
                << "cat input.txt | ./main > output.txt" << std::endl
                << "./main input.txt > output.txt" << std::endl
                << "./main input.txt output.txt" << std::endl;
            return 1;
    }
    processAllCases(*is, *os);
    return 0;
}

bool palindrome(const int number);

// process all cases
void processAllCases(std::istream &is, std::ostream &os)
{
    std::set<long long> preCalculatedFairAndSquare;
    double maximum(sqrt(10e14));
    long long maximumInteger = static_cast<long long>(maximum);
    for(long long i = 1LL; i <= maximumInteger; i++)
    {
        if(palindrome(i))
        {
            long long squared = i*i;
            if (palindrome(squared))
            {
                preCalculatedFairAndSquare.insert(squared);

            }
        }
    }
    int totalCases;
    is >> totalCases;
    for(int caseNumber = 1; caseNumber <= totalCases; ++caseNumber)
    {
        processCase(caseNumber, is, os, preCalculatedFairAndSquare);
    }
}


// process individual case, caseNumber = 1..totalCases
void processCase(const int caseNumber, std::istream &is, std::ostream &os, const std::set<long long> &preCalculatedFairAndSquare)
{
    long long lowerRange;
    long long upperRange;
    is >> lowerRange;
    is >> upperRange;

    os << "Case #" << caseNumber << ": " << std::distance(preCalculatedFairAndSquare.lower_bound(lowerRange), preCalculatedFairAndSquare.upper_bound(upperRange)) << std::endl;
    // only change this function for codejam problems
}

bool symmetricalString(const std::string &s)
{
    return std::equal(s.begin(), s.begin() + s.size()/2, s.rbegin());
}

bool palindrome(int number)
{
    std::stringstream ss;
    ss << number;
    std::string str = ss.str();
    return symmetricalString(str);
}

