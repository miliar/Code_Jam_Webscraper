#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <map>
#include <list>
#include <vector>

////////////////////////////////////////////////////////////
// Input
// Output
////////////////////////////////////////////////////////////

namespace
{
    static std::ofstream &GetOut()
    {
        static std::ofstream C_OUT("out.txt", std::ofstream::out);
        return C_OUT;
    }

    static std::ifstream &GetIn()
    {
        static std::ifstream C_IN;
        return C_IN;
    }
}

////////////////////////////////////////////////////////////
// Problem specific data
////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////
// Problem
////////////////////////////////////////////////////////////

class Problem
{
public:
    Problem();
    ~Problem();

    const std::string& getSolution();
private:
    int r_sMax;
    std::vector<int>  r_shyLevel;
    std::string r_solution;

    void solveProblem();
};

Problem::Problem()
 : r_sMax(0),
   r_shyLevel(),
   r_solution("")
{
    //would read the problem data from input file
    GetIn() >> r_sMax;

    std::string shyLevel;
    GetIn() >> shyLevel;

    const char* s = shyLevel.c_str();
    for(int i = 0; i <= r_sMax; ++i)
    {
        r_shyLevel.push_back(s[i] - '0');
    }
}

Problem::~Problem()
{
}

const std::string& Problem::getSolution()
{
    solveProblem();
    return r_solution;
}

void Problem::solveProblem()
{
    if(r_sMax == 0)
    {
        r_solution = "0";
        return;
    }

    int extra = 0;
    int total = 0;

    for(int i = 0; i <= r_sMax; ++i)
    {
        if((total + extra) >= i)
        {
            total += r_shyLevel[i];
        }
        else
        {
            total += r_shyLevel[i];
            ++extra;
        }
    }

    r_solution = std::to_string(extra);
}
////////////////////////////////////////////////////////////
// Test case
////////////////////////////////////////////////////////////

class TestCase
{
public:
    TestCase(int iCaseNumber)
    {
        std::cout << "\t\t -- Process Test Case: " << iCaseNumber 
            << " --"<<std::endl;

        auto solution = Problem().getSolution();

        std::cout << "Case #" << iCaseNumber << ": "
            << solution.c_str() << std::endl;

        GetOut() << "Case #" << iCaseNumber << ": "
            << solution.c_str() << std::endl;
    }
    ~TestCase(){}
};

////////////////////////////////////////////////////////////
// The problem solver
////////////////////////////////////////////////////////////

class ProblemSolver
{
public:
    ProblemSolver(const std::string &iInputFile)
    {
        GetIn().open(iInputFile, std::ifstream::in);

        if(false == GetIn().good())
        {
            std::cout << "read file failed\n";
            return;
        }
        else
        {
            int nbOfTestCases = 0;
            GetIn() >> nbOfTestCases;

            std::cout << "Test cases: " << nbOfTestCases << std::endl;

            for(int i = 1; i <= nbOfTestCases; ++i)
            {
                TestCase t(i);
            }
        }
    }

    ~ProblemSolver() 
    {
        GetIn().close();
        GetOut().close();
    }

private:
};

void readInput();
void openOutput();
void findItems(TestCase testCase);
void closeOutput();

////////////////////////////////////////////////////////////
// main function
////////////////////////////////////////////////////////////

int main()
{
    //ProblemSolver("downloads/test.in");
    //ProblemSolver("downloads/A-small-attempt0.in");
    ProblemSolver("downloads/A-large.in");

    return 0;
}
