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
    unsigned int n;
    inpStream >> n;
    string value;
    vector<string> fegla;
    for (unsigned int i = 0; i < n; ++i)
    {
        inpStream >> value;
        fegla.push_back(value);
    }
    unsigned int operationsPerformed = 0;
    while (!SingleCaseProcessed(n, fegla))
    {
        // get the character we will be solving
        if (fegla[0].size() == 0)
        {
            outStream << "Case #" << t + 1 << ": " << "Fegla Won" << endl;
            return;
        }
        char charToProcess = fegla[0][0];
        // in each step, go through all the strings and count the number of same characters at the beginning
        vector<unsigned int> importantCharsCount(n, 0);
        for (unsigned int i = 0; i < n; ++i)
        {
            // remove the important chars from the string
            while (fegla[i].size() && fegla[i][0] == charToProcess)
            {
                ++importantCharsCount[i];
                fegla[i].erase(0, 1);
            }
        }
        // get the target number of characters - the average from the string
        long double avg = 0.0;
        for (unsigned int i = 0; i < n; ++i)
        {
            if (!importantCharsCount[i])
            {
                // some string did not contain the important char
                outStream << "Case #" << t + 1 << ": " << "Fegla Won" << endl;
                return;
            }
            avg += importantCharsCount[i];
        }
        avg /= n;
        unsigned int targetNumOfImportantChars = (unsigned int)(avg + 0.5);
        // get the number of operations needed
        for (unsigned int i = 0; i < n; ++i)
        {
            if (importantCharsCount[i] > targetNumOfImportantChars)
                operationsPerformed += importantCharsCount[i] - targetNumOfImportantChars;
            else
                operationsPerformed += targetNumOfImportantChars - importantCharsCount[i];
        }
    }
    outStream << "Case #" << t + 1 << ": " << operationsPerformed << endl;
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
