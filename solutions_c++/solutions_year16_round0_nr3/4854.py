#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <string>
#include <inttypes.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

/*
***
The program to generate jam coin like numbers but not satisfying the 3rd condition.
It generates all such 16 bit numbers ina  file called binarynums.txt and then we use that file for 
further procedure 
***

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
*/

cpp_int isPrime(cpp_int n)
{
      for(cpp_int fact=2; fact*fact<=n; fact+=1 ){
        if(n%fact==0)
          return fact;
      }
      return -1;
}

void ConvertBinary2Decimal(cpp_int s)
{
  ofstream outfile;
  outfile.open("nonprimenumsconverted.txt", std::ios_base::app);
  cpp_int numbers[10];
  int k=0,flag=1;
  for(int b=2;b<11;b++)
  {
      memset(numbers, 0 , 10);
      cpp_int decimal = 0;
      cpp_int remainder=0; 
      cpp_int base = 1;
      cpp_int temp = s;
      //int len=s.length();
      //for (int i = len-1; i >= 0; i--)
      while(temp>0)
      {
          remainder = temp % 10;
          decimal = decimal + remainder * base;
          base = base * b;
          temp = temp/10;

      }
      cpp_int ans=isPrime(decimal);
      if(ans!=-1)
      {
        if(b==2)
        {
           numbers[k++] = s;
           numbers[k++] = ans;
          //outfile<<s<<" "<<decimal<<" ";
        }
         
        else if(b>2 && b<=10)
        {
          //outfile<<decimal<<" ";
          numbers[k++] = ans;
        }
        
      }
      else
      {
        flag=0;
      } 
  }
  if(flag==0)
      return;
  else
  {
        outfile<<s<<" ";
        for(int q=1; q<9 ; q++)
        {
          outfile<<numbers[q]<<" ";
        }
        outfile<<numbers[9]<<"\n";
  }
  outfile.close();
}

int main()
{
	int t;
	long long num;
	cpp_int s;
	ifstream myfile ("binarynums.txt");
	if (myfile.is_open())
  	{
  		//myfile >> t;
	    while(myfile>>s){
        //int flag = 0;
        ConvertBinary2Decimal(s);
	    }
		  myfile.close();
  	}
	return 0;
}