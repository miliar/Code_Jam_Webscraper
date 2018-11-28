#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
#include<stdlib.h>
#define SIZE 100
using namespace std;
string convertInt(int);
int fair_square(int);
int Palindrome(string);
int main()
{
  int x=1;
  int test;
  int T, k, count;
  int low_bound,upper_bound;
  ifstream input;
  ofstream output;
  input.open("C-small-attempt0.in");
  output.open("output.txt");
  input >> T;
  if(T>=1 && T<=SIZE)
  {
  for(k=1; k<=T; k++)
 {
  input >> low_bound;
  input >> upper_bound;
  if((low_bound >=1 && low_bound <=upper_bound) && (upper_bound <= 1000))
  {
  count = 0;
  for(x=low_bound; x<=upper_bound; x++)
   { 
   test  = fair_square(x);
    if(test != -1)
     count++;
   }
 output << "Case #" << k << ": " << count << "\n";
 }
  else
     exit(1);
}
}

input.close();
output.close();
  
 return 0;
}

string convertInt(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

int fair_square(int x)
{ 
 string str;
 string strs;
 int ret_val;
 int chk = 0;
 double d_sqrt = sqrt(x);
 int i_sqrt = d_sqrt;
 if ( d_sqrt == i_sqrt )
   {
     str = convertInt(x);
     chk = Palindrome(str);
     if(chk != - 1)
      {
      strs = convertInt(i_sqrt);
      chk = Palindrome(strs);
        if(chk != -1)
            ret_val = 1;
        else
            ret_val = -1;
      }
      else
         ret_val = -1;
   }
  else
    ret_val = -1;
 return ret_val; 
}


int Palindrome(string str)
{
 int i=0;
 int len = str.size() - 1;
 while(i<=len)
  {
    if(str[i] != str[len])
     break;

   i++;
   len--;
  }

  if(i >= len)
   return 1;
  else
   return -1;
}
