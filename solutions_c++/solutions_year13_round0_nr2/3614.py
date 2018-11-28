#include <cstdio>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct TestCase
{
    unsigned Width;
    unsigned Height;

    vector<unsigned> Lawn;
};

unsigned valueAt(const TestCase &_testCase, unsigned _x, unsigned _y)
{
    return _testCase.Lawn[_x + _y * _testCase.Width];
}

bool checkRow(const TestCase &_testCase, unsigned _y, unsigned _ref)
{
    for(unsigned i = 0; i < _testCase.Width; ++i)
    {
        if(valueAt(_testCase, i, _y) > _ref)
            return false;
    }

    return true;
}

bool checkColumn(const TestCase &_testCase, unsigned _x, unsigned _ref)
{
    for(unsigned i = 0; i < _testCase.Height; ++i)
    {
        if(valueAt(_testCase, _x, i) > _ref)
            return false;
    }

    return true;
}

bool checkLawnCase(const TestCase &_testCase, unsigned _x, unsigned _y)
{
    const unsigned ref = valueAt(_testCase, _x, _y);

    return checkRow(_testCase, _y, ref) || checkColumn(_testCase, _x, ref);
}

bool checkTestCase(const TestCase &_testCase)
{
    for(unsigned y = 0; y < _testCase.Height; ++y)
    {
        for(unsigned x = 0; x < _testCase.Width; ++x)
        {
            if(!checkLawnCase(_testCase, x, y))
                return false;
        }
    }

    return true;
}

void parseTestCase(istream &_input, TestCase &_testCase)
{
    string buffer;

    getline(_input, buffer);
    sscanf(buffer.c_str(), "%d %d", &_testCase.Height, &_testCase.Width);

    for(unsigned i = 0; i < _testCase.Height; ++i)
    {
        getline(_input, buffer);

        const char *strPtr = buffer.c_str();
        for(unsigned j = 0; j < _testCase.Width; ++j)
        {
            _testCase.Lawn.push_back(atoi(strPtr));
            strPtr = strchr(strPtr, ' ') + 1;
        }
    }
}

void parseInput(vector<TestCase> &_testCases, const char *_fileName)
{
    fstream input(_fileName, fstream::in);

    string buffer;
    getline(input, buffer);

    const unsigned length = atoi(buffer.c_str());

    _testCases.reserve(length);
    for(unsigned i = 0; i < length; ++i)
    {
        TestCase testCase;
        parseTestCase(input, testCase);

        _testCases.push_back(testCase);
    }

    input.close();
}

void displayResult(FILE *_outFile, unsigned _caseIndex, bool _result)
{
    fprintf(_outFile, "Case #%d: %s\n", _caseIndex + 1, _result ? "YES" : "NO");
}

void computeOutput(const vector<TestCase> &_testCases)
{
    FILE *output = fopen("output", "w");

    const unsigned length = _testCases.size();
    for(unsigned i = 0; i < length; ++i)
    {
        displayResult(output, i, checkTestCase(_testCases[i]));
    }

    fclose(output);
}

int main(int argc, char *argv[])
{
    if(argc != 2)
        return -1;

    vector<TestCase> testCases;
    parseInput(testCases, argv[1]);
    computeOutput(testCases);

    return 0;
}