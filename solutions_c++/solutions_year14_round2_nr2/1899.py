#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

using namespace std;

/// Duplicator of output into two different streams.
class CDoubleOutput
{
public:
    CDoubleOutput(ostream &stream1, ostream &stream2): stream1(stream1), stream2(stream2) { }
    
    /// normal output operator
    template<typename T>
    CDoubleOutput& operator<<(const T &value)
    {
        stream1 << value;
        stream2 << value;
        return *this;
    }
    /// operator that helps with manipulators
    CDoubleOutput& operator<<(std::ostream &(*fmanip)(std::ostream &))
    {
        fmanip(stream1);
        fmanip(stream2);
        return *this;
    }
    
private:
    ostream &stream1;
    ostream &stream2;
};

// returns true when all the strings inside the vector are of a zero length
bool SingleCaseProcessed(unsigned int n, vector<string> &fegla)
{
    for (unsigned int i = 0; i < n; ++i)
    {
        if (fegla[i].size())
            return false;
    }
    return true;
}

void SolveTestCase(int t, istream& inpStream, CDoubleOutput& outStream)
{
    // read the input first
    unsigned int a, b, k;
    inpStream >> a >> b >> k;
    
    unsigned int numOfOKCombinations = 0;
    for (unsigned int aa = 0; aa < a; ++aa)
    {
        for (unsigned int bb = 0; bb < b; ++bb)
        {
            unsigned int cc = aa & bb;
            if (cc < k)
                ++numOfOKCombinations;
        }
    }
    outStream << "Case #" << t + 1 << ": " << numOfOKCombinations << endl;
}

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        cerr << "No input file!" << endl;
        return 1;
    }
    ifstream inputFile(argv[1]);
    string outputFileName(argv[1]);
    outputFileName.replace(outputFileName.length() - 3, 3, ".out"); // ok, we know we do not need to check here
    ofstream outputFile(outputFileName);
    CDoubleOutput outputStream(cout, outputFile);
    unsigned int n;
    inputFile >> n;
    for (unsigned int i = 0; i < n; ++i)
        SolveTestCase(i, inputFile, outputStream);
    outputFile.flush();
    outputFile.close();
    return 0;
}
