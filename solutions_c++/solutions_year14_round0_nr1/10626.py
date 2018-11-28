#include <iostream>
#include <fstream>

using namespace std;

struct testCase
{
  int answer1;
  int answer2;
  
  int arrangement1[4][4];
  int arrangement2[4][4];
  
  testCase()
  {
    answer1 = 0;
    answer2 = 0;
    
    for(int i = 0; i < 4; i++)
    {
      for(int j = 0; j < 4; j++)
      {
	arrangement1[i][j] = 0;
	arrangement2[i][j] = 0;
      }
    }
  }
};

/*void test(testCase &casex)
{
  cout<<casex.answer1<<endl;
  
  for(int i = 0; i < 4; i++)
  {
    for(int j = 0; j < 4; j++)
    {
      cout<<casex.arrangement1[i][j]<<" ";
    }
    
    cout<<endl;
  }
  
  cout<<casex.answer2<<endl;
  
  for(int i = 0; i < 4; i++)
  {
    for(int j = 0; j < 4; j++)
    {
      cout<<casex.arrangement2[i][j]<<" ";
    }
    
    cout<<endl;
  }
}*/

void processIT(testCase casex, ofstream &output, int caseNumber)
{
  int foundCount = 0; int num = 0;
  
  for(int i = 0; i < 4; i++)
  {
    for(int j = 0; j < 4; j++)
    {
      if(casex.arrangement1[casex.answer1-1][i] == casex.arrangement2[casex.answer2-1][j])
      {
	foundCount++; num = casex.arrangement1[casex.answer1-1][i];
      }
    }
  }
  
  if(foundCount == 0)
  {
    output<<"Case #"<<caseNumber<<": Volunteer cheated!"<<endl;
  }
  
  else if(foundCount == 1)
  {
    output<<"Case #"<<caseNumber<<": "<<num<<endl;
  }
  
  else if(foundCount > 1)
  {
    output<<"Case #"<<caseNumber<<": Bad magician!"<<endl;;
  }
}

int main()
{
  ifstream input("sample.txt");
  ofstream output("output.txt");
  
  int NoOfTestCases;	
  input>>NoOfTestCases;
  
  testCase cases[NoOfTestCases];
  
  for(int i = 0; i < NoOfTestCases; i++)
  {
    input>>cases[i].answer1;
	    
    for(int j = 0; j < 4; j++)
    {
      for(int k = 0; k < 4; k++)
      {
	input>>cases[i].arrangement1[j][k];
      }
    }
    
    input>>cases[i].answer2;
	    
    for(int j = 0; j < 4; j++)
    {
      for(int k = 0; k < 4; k++)
      {
	input>>cases[i].arrangement2[j][k];
      }
    }
    
    //test(cases[i]);
    processIT(cases[i], output, i+1);
  }
  
  
  
  return 0;
}
