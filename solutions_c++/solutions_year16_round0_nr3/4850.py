#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <string>
#include <inttypes.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

cpp_int returnFactor(cpp_int n)
{
    
      for(cpp_int u=2; u*u<=n; u+=1 ){
        if(n%u==0)
          return u;
      }
      return -1;
}

cpp_int ConvertBinary2Decimal(cpp_int s, int b)
{
      cpp_int decimal = 0;
      cpp_int remainder=0; 
      cpp_int base = 1;
      cpp_int temp = s;
      while(temp>0)
      {
          remainder = temp % 10;
          decimal = decimal + remainder * base;
          base = base * b;
          temp = temp/10;

      }
      cpp_int ans = returnFactor(decimal);
      return ans;
      
}

int main()
{
  int t,k=0;
  long long num;
  cpp_int numbers[10];
  cpp_int factor;
  cpp_int s,flag;
  ifstream myfile ("binarynums.txt");
   ofstream outfile;
  outfile.open("output.txt", std::ios_base::app);
  outfile<<"Case #1:"<<endl;
  if (myfile.is_open())
    {
      myfile >> t;
      while(myfile>>s){
          memset(numbers,0,10);
          flag=0;
          numbers[0] = s;
          for(int i=2;i<11;i++){
            factor = ConvertBinary2Decimal(s,i);
            if(factor==-1)
             { 
              flag=1;
              break;
            }
            else
            numbers[++k]=factor;
          }
          if(flag!=1)
          {
               outfile<<s<<" ";
               for(int q =1 ; q<9 ; q++)
                {
                  outfile<<numbers[q]<<" ";
                }
                outfile<<numbers[9]<<"\n";
          }
      }
      myfile.close();
    }
  return 0;
}
/*


void bin(unsigned n)
{
    if (n > 1)
        bin(n/2);
 
    ofstream outfile;

    outfile.open("binarynums.txt", std::ios_base::app);
    outfile << n % 2;
    outfile.close();
}
 
int main(void)
{
    for(int i = 32769; i<=65535; i+=2)
    {
      bin(i);
      ofstream outfile;

      outfile.open("binarynums.txt", std::ios_base::app);
      outfile << endl;
      outfile.close();
    }
    
  return 0;
}

***
The above program is to generate jam coin like numbers but not satisfying the last condition.
It generates all 16 bit numbers in a  file called binarynums.txt and then we use that file for 
further procedure in our program.
***
*/