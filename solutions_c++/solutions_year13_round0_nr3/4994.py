/**********************
*    Author: Lin Qi
*    Date: Jan. 27 2013
***********************/


#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;


bool isPalindrome(int n)
{
  if(n < 10)
    return true;

  int *digits = new int[n];
  int index = 0;
  while ( n > 0)
  {
    digits[index++] = n % 10;
    n = n /10;
  }
  int i=0, j=index-1;
  while( i < j )
  {
    if(digits[i] != digits[j])
      return false;
    i++;
    j--;
  }
  return true;

}

int main()
{
  int nString;
  string inputFileName = "input.txt";
  string outputFileName = "output.txt";
  ifstream infile;
  ofstream ofile;

  //Loading information
  infile.open(inputFileName.c_str());
  ofile.open(outputFileName.c_str());
  if (!infile.is_open())
  {
    cout <<"Unable to open file \""<< inputFileName.c_str() << "\"."<<endl;
    exit(1);
  }

  infile >> nString;
  char sstring[100];
  infile.getline(sstring, 100);

  for(int numStr = 0; numStr < nString; numStr++)
  {
    cout<<"Case #"<<numStr + 1<<""<<": ";
    int counter = 0;
    int small, large;
    infile >> small;
    infile >> large;

    // cout<<small<<" "<<large<<endl;

    for(int i = small; i <= large; i++)
    {
      if(isPalindrome(i))
      {
        float f = sqrt(double(i));
        if( f == int(f) && isPalindrome(f) ) 
        {
          counter++;

        }

      }
    }
    cout<<counter<<endl;

  }
  infile.close();
  ofile.close();
  return 0;
}