#include "ProblemInterface.h"
#include <memory>
#include <iostream>

// do all includes here
#include "2013QualificationRound.h"
#include "2015QualificationRound.h"
#include "2014Round1C.h"

// change define to current problem class name
#define PROBLEM_TYPE qualificationRound2015::A

static const char* InputLarge = "large.in";
static const char* InputSmall = "small.in";

class Output
{
public:
    Output(const std::string &filename)
    {
        m_File.open(filename, std::ios::out);
    }

    void write(const std::string& out)
    {
        BOOST_ASSERT_MSG(!out.empty(), "output is empty");
        ++m_uiRound;
        m_File << "Case #" << m_uiRound << ": " << out << std::endl;
        std::cout << "Case #" << m_uiRound << ": " << out << "\n";
    }

private:
    uint32 m_uiRound = 0;
    std::ofstream m_File;
};

int main()
{
    auto pProblem = std::make_unique<PROBLEM_TYPE>();
    Input input;
    try
    {
        input.open(pProblem->getInputDir() + InputLarge);
    }
    catch (const std::exception&)
    {
        input.open(pProblem->getInputDir() + InputSmall);
    }

    // output
    Output output("jam.out");
    for (uint32 i = 0; i < input.getDataSetCount(); ++i)
        output.write(pProblem->next(input));

    std::cin.get();
}