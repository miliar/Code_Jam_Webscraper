#include <cstdio>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct TestCase
{
    unsigned Min;
    unsigned Max;
};

bool isPalindrome(unsigned _number)
{
    if(_number % 10 == 0)
        return false;

    unsigned buffer = 0;
    while(_number > buffer)
    {
        buffer = buffer * 10 + _number % 10;
        _number /= 10;
    }

    return _number == buffer || _number == buffer / 10;
}

bool isSquarePalindrome(unsigned _number)
{
    unsigned buffer = 0;
    while(_number > 0 && buffer < 10)
    {
        const unsigned digit = _number % 10;
        buffer += digit * digit;
        _number /= 10;
    }

    return buffer < 10;
}

unsigned computeTestCase(const TestCase &_testCase)
{
    const unsigned start = (unsigned)ceil(sqrt((float)_testCase.Min));
    const unsigned end = (unsigned)floor(sqrt((float)_testCase.Max));

    printf("\n%u %u\n", _testCase.Min, _testCase.Max);

    unsigned count = 0;
    for(unsigned i = start; i <= end; ++i)
    {
        //if(isPalindrome(i) && isPalindrome(i * i))
        if(isPalindrome(i) && isSquarePalindrome(i))
        {
            count++;
            printf("%u %u\n", i, i * i);
        }
    }

    return count;
}

void parseTestCase(istream &_input, TestCase &_testCase)
{
    string buffer;

    getline(_input, buffer);
    sscanf(buffer.c_str(), "%d %d", &_testCase.Min, &_testCase.Max);
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

void displayResult(FILE *_outFile, unsigned _caseIndex, unsigned _result)
{
    fprintf(_outFile, "Case #%d: %d\n", _caseIndex + 1, _result);
}

void computeOutput(const vector<TestCase> &_testCases)
{
    FILE *output = fopen("output", "w");

    const unsigned length = _testCases.size();
    for(unsigned i = 0; i < length; ++i)
    {
        displayResult(output, i, computeTestCase(_testCases[i]));
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