#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
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

void SolveTestCase(int n, istream& inpStream, CDoubleOutput& outStream)
{
    // read input
    unsigned int sMax;
    inpStream >> sMax;
    string shinessHistogramStr = string();
    inpStream >> shinessHistogramStr;
    vector<unsigned char> shinessHistogram = vector<unsigned char>(sMax + 1);
    for (unsigned int i = 0; i < shinessHistogram.size(); ++i)
        shinessHistogram[i] = shinessHistogramStr[i] - '0';
    // process the input
    unsigned int numOfStandingNormally = 0;
    unsigned int numOfStandingAdded = 0;
    for (unsigned int i = 0; i < shinessHistogram.size(); ++i)
    {
        unsigned int numOfStanding = numOfStandingNormally + numOfStandingAdded;
        // do we have to add people?
        if (numOfStanding < i && shinessHistogram[i] != 0)
        {
            numOfStandingAdded += (i - numOfStanding);
        }
        numOfStandingNormally += shinessHistogram[i];
    }
    
    // print out the result
    outStream << "Case #" << n + 1 << ": ";
    outStream << numOfStandingAdded;
    outStream << endl;
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
