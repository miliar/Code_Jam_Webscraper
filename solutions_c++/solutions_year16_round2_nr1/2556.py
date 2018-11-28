#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
  ifstream myInput;
  myInput.open("A-large.in");
  ofstream myOutput;
  myOutput.open("solution.out");

  int t;
  double c;
  double f;
  double x;

  myInput >> t;
  for(int i = 0; i < t; i++)
  {
    string jumble;
    myInput >> jumble;
    int array[26];
    for(int k = 0; k < 26; k++)
      array[k] = 0;
    for(int j = 0; j < jumble.length(); j++)
      array[jumble[j] - 65]++;
    myOutput << endl;
    int number[10];
    for(int k = 0; k < 10; k++)
      number[k] = 0;
    while(array[25])
    {
      number[0]++;
      array[25]--; //z
      array[4]--; //e
      array[17]--; //r
      array[14]--; //o
    }
    while(array[23])
    {
      number[6]++;
      array[18]--; //s
      array[8]--; //i
      array[23]--; //x
    }
    while(array[18])
    {
      number[7]++;
      array[18]--; //s
      array[4] -= 2; //e
      array[13]--; //n
      array[21]--; //v
    }
    while(array[21])
    {
      number[5]++;
      array[5]--; //f
      array[8]--; //i
      array[4]--; //e
      array[21]--; //v
    }
    while(array[5])
    {
      number[4]++;
      array[14]--; //o
      array[20]--; //u
      array[17]--; //r
      array[5]--; //f
    }
    while(array[17])
    {
      number[3]++;
      array[19]--; //t
      array[7]--; //h
      array[4] -= 2; //e
      array[17]--; //r
    }
    while(array[7])
    {
      number[8]++;
      array[4]--; //e
      array[8]--; //i
      array[6]--; //g
      array[19]--; //t
      array[7]--; //h
    }
    while(array[19])
    {
      number[2]++;
      array[22]--; //w
      array[14]--; //o
      array[19]--; //t
    }
    number[1] += array[14];
    number[9] += array[8];

    myOutput << "Case #" << i + 1 << ": ";
    for(int k = 0; k < 10; k++)
      for(int m = 0; m < number[k]; m++)
        myOutput << k;
    myOutput << endl;
  }
}
