#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
  ifstream myInput;
  myInput.open("B-large.in");
  ofstream myOutput;
  myOutput.open("solution.out");

  int t;
  myInput >> t;
  for(int i = 0; i < t; i++)
  {
    char last = 'x';
    string input;
    myInput >> input;
    int count = 0;

    for(int j = 0; j < input.length(); j++)
    {
      if(input[j] != last)
        count++;
      last = input[j];
    }
    if(input[input.length() - 1] == '+')
      count--;
    myOutput << "Case #" << i + 1 << ": " << count << endl;
  }
}
