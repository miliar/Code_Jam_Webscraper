#include <iostream>
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

typedef std::vector<int> RowNbs;

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
    int         r_P;
    int         r_Q;
    std::string r_solution;

    void solveProblem();
};

Problem::Problem() 
 : r_P(0),
   r_Q(0),
   r_solution("")
{
    //would read the problem data from input file
    char slash = '1';
    GetIn() >> r_P;
    GetIn() >> slash;
    GetIn() >> r_Q;
}

void simplify(int &a, int &b)
{
    int p = a;
    int q = b;
    for(int i = 2; i < (b/2 + 1); )
    {
        if(p%i == 0 &&
           q%i == 0)
        {
            p /= i;
            q /= i;
        }
        else
        {
            ++i;
        }
    }

    a = p;
    b = q;
}

bool multipleOf2(int a)
{
    bool result = false;

    int pow = 1;
    int nb = 2;

    while(nb != a &&
          nb < a)
    {
        nb = 2* nb;
        ++pow;
    }

    result = nb == a;

    return result;
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
    if(r_Q%2 != 0)
    {
        r_solution = "impossible";
        return;
    }

    if(false == multipleOf2(r_Q))
    {
        r_solution = "impossible";
        return;
    }

    simplify(r_P, r_Q);

    int gen = 0;
    do
    {
        if(r_P > r_Q/2)
        {
            r_solution = std::to_string(gen + 1);
            return;
        }

    //    std::cout << "p: " << r_P << std::endl;
      //  std::cout << "q: " << r_Q << std::endl;

        if(r_P == 1)
        {
            int pow = 1;
            int nb = 2;

            while(nb != r_Q &&
                  nb < r_Q)
            {
                nb = 2* nb;
                ++pow;
            }

            if(nb > r_Q)
            {
                r_solution = "impossible";
            }
            r_solution = std::to_string(pow + gen);
            return;
        }

        ++gen;
        r_Q = r_Q / 2;
    } while (true);
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

void main()
{
    //ProblemSolver("test.txt");
    ProblemSolver("A-small-attempt0.in");
    //ProblemSolver("A-large-practice.in");
    getchar();
}
