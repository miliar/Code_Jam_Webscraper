#include "CountingSheep.h"

CCountingSheep::CCountingSheep() : CProblem("CountingSheep")
{
}

CCountingSheep::~CCountingSheep()
{
}

bool CCountingSheep::SolveInput(const std::string& i_Input, const std::string& i_Output)
{
  std::string Output;

  bool Res = OpenInput(i_Input);
  RETURN_IF_FAILED(Res);

  int32_t NumberOfCases = 0;
  Res = m_FileReader.ReadLineInteger(NumberOfCases);
  RETURN_IF_FAILED(Res);

  for(int32_t i = 1; NumberOfCases >= i; ++i)
  {
    m_DigitOccurence.reset();
    std::string CaseOutput;
    
    int32_t Number = 0;
    Res = m_FileReader.ReadLineInteger(Number);

    if(0 >= Number)
    {
      CaseOutput = "INSOMNIA";
    }
    else
    {
      int32_t N = 0;
      int32_t NumberToSpilt = Number;
      int32_t LastNumber = NumberToSpilt;

      do
      {
        ++N;
        NumberToSpilt = N * Number;
        LastNumber = NumberToSpilt;

        do
        {
          int32_t Digit = NumberToSpilt % 10;
          m_DigitOccurence[Digit] = true;
          NumberToSpilt /= 10;
        } while(NumberToSpilt > 0);
      } while(!m_DigitOccurence.all());


      CaseOutput = std::to_string(LastNumber);
    }

    Output += GenerateOutput(i, CaseOutput);
  }

  Res = m_FileWriter.Write(i_Output, Output);
  RETURN_IF_FAILED(Res);

  return Res;
}

std::string CCountingSheep::GenerateOutput(int32_t i_CaseNumber, const std::string& i_CaseOutput)
{
  std::string Output = CProblem::GenerateOutputPrefix(i_CaseNumber) + i_CaseOutput + "\n";
  return Output;
}
