
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <math.h>
using namespace std;
int numDigits(int number)
{
    int digits = 0;
    if (number < 0) digits = 1; // remove this line if '-' counts as a digit
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}
bool is_palindrom(int input)
{
int digits=numDigits(input);
int temp,temp1;
if(digits==1)
    return true;
for(int i=1;i<=(digits/2);i++)
{
    temp=input%((int) pow10(i));
    temp1=input/( (int) pow10(digits-i));
    if(temp!=temp1)
       { return false;}
}
    return true;
}
int main()
{
   ofstream output;
  string line;
  int min,max;
  int number_tests;
  double checker_d;
  int checker_int;
    output.open ("output.txt");
    fstream input("input.txt");
    int counter;
     if (output.is_open())
     {
    if (input.is_open())
    {
     if( input.good() )
      {
         getline(input,line);
         number_tests=atoi(line.c_str());
         for(int i=1;i<=number_tests;i++)
         {
             counter=0;
             input>>min;
             input>>max;
             for(int j=min;j<=max;j++)
             {
                 checker_d=sqrt(j);
                 checker_int=checker_d;
                 if(is_palindrom(j))
                 {
                 if(checker_int==checker_d && is_palindrom(checker_int))
                     counter++;
                 }
             }
             output<<"Case #"<<i<<": "<<counter<<endl;
         }
     }
     output.close();
      input.close();
    }
    else cout << "Unable to open input.txt file";
     }
     else
    cout << "Unable to open file output.txt!" << endl;
    return 0;
}

