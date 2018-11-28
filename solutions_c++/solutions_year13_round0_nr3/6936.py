#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

long long sqrootnum;

bool isapalindrome (long long num)
{
   unsigned long long dig,rev,n;
   n= num;
   rev=0;
   while (n > 0)
   {
         dig = n %10;
         rev = rev* 10 + dig;
         n= n/10;
            
   }
    if (num==rev) return true; else return false;
   
}

bool isaperfectsquare(long long num)
{
     
     sqrootnum = sqrt (num);
     if ((sqrootnum * sqrootnum)== num) return true;
     else 
     return false;
 }
 
int main()
{
      unsigned int T, tCase;
      unsigned long long A, B,i,count;
      ifstream inFile;
      ofstream outFile;
      inFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small.in");
      outFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small-out.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          count = 0;
          inFile >> A;
          inFile >> B;
          for (i=A; i <= B; i++)
          {
             if (isapalindrome(i) == true)
                if (isaperfectsquare(i) == true)
                {
                 if (isapalindrome(sqrootnum) == true)
                    count++;
                }
          }
          outFile << "Case #" << tCase << ": " << count << "\n";          
      }

}


