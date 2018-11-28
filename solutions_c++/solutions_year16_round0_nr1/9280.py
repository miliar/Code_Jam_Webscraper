#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

vector<int> input;
set<int> resultset;
int testnum;

void putDigitToResult(int n)
{
    do
    {
      int digit = n % 10;
      //result[digit] = true;
      resultset.insert(digit);
      n /= 10;
    } while (n > 0);
    /*bool l=true;
    while (l)
    {

    }*/
}
bool alldigitsdone()
{
    return resultset.size()==10;
}
bool isItInsomnia(int counter)
{
    return (counter>2000);
}
void doItForANumber(ofstream& file,int N,int casecount)
{
    int originalN=N;

    bool insomnia = false;
    int counter = 0;

    while (true)
    {
        counter++;
        putDigitToResult(N);
        if (alldigitsdone())
        {
            break;
        }
        N=N+originalN;
        if (isItInsomnia(counter))
        {
            insomnia=true;
            break;
        }
    }

    //cout << "originalN: " << originalN <<" laterN: "<<N<<" insomnia: "<<insomnia<<" counter: "<<counter<< endl;
    file << "Case #"<<casecount<<": ";
    if (insomnia)
    {
        file << "INSOMNIA";
    }
    else
    {
        file << N;
    }
}

bool getInput()
{
  string testcases;
  string onecase;
  ifstream inputfile("input.txt");
  if (inputfile.is_open())
  {
    getline (inputfile, testcases);
    testnum = atoi(testcases.c_str());
    for (int i=0;i<testnum;i++)
    {
      getline (inputfile, onecase);
      {
        int casenum=atoi(onecase.c_str());
        input.push_back(casenum);
      }
    }
    inputfile.close();
    return true;
  }
  else
  {
      cout << "Unable to open file";
      return false;
  }
}
int main()
{
  testnum = 0;
  getInput();
  ofstream filename ("output.txt");
  if (filename.is_open())
  {
    for (int i=0;i<testnum;i++)
    {
      doItForANumber(filename,input[i],i+1);
      resultset.clear();
      if (i!=testnum-1)
      {
          filename <<"\n";
      }
    }
    filename.close();
  }
  else cout << "Unable to open file";

  return 0;
}
