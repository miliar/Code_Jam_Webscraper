#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <fstream>
using namespace std;

vector<vector<bool> > input;
int testnum;

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
      vector<bool> arr;
      {
        for (int i=0;i<onecase.size();i++)
        {
          if (onecase[i]=='+')
          {
            arr.push_back(true);
          }
          if (onecase[i]=='-')
          {
            arr.push_back(false);
          }
        }
        input.push_back(arr);
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
  testnum=0;
  getInput();
  ofstream filename ("output.txt");
  filename.is_open();
  for (int j=0;j<testnum;j++)
  {
    int switchcounter=0;
    int length = input[j].size();
    int counter = length-1;

    while (counter>-1)
    {
      if (input[j][counter])
      {
        counter--;
      }
      else
      {
        for (int k=counter;k>-1;k--)
        {
          input[j][k]=!input[j][k];
        }
        switchcounter++;
        counter--;
      }
    }
    //cout << switchcounter<<endl;
    filename << "Case #"<<j+1<<": "<<switchcounter;
    if (j!=testnum-1)
      {
          filename <<"\n";
      }
  }
  return 0;
}
