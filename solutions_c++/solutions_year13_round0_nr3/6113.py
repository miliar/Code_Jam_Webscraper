#include<iostream>
#include<cmath>
#include <sstream>
using namespace std;
bool IsFairAndSquare(int);
int main()
{
int NumberOfCases;
int CurrentCase;
int FairMin;
int FairMax;
int NumberOfFairAndSquare;
int i;
cin >>NumberOfCases;
for(CurrentCase=1;CurrentCase<=NumberOfCases;CurrentCase++)
 {
  cin>> FairMin;
  cin >> FairMax;
  NumberOfFairAndSquare=0;
  for (i=FairMin;i<=FairMax;i++)
    if(IsFairAndSquare(i))NumberOfFairAndSquare++;
  cout <<"Case #"<<CurrentCase<<": " <<NumberOfFairAndSquare<<endl;
 }
}
bool IsFairAndSquare(int x)
{
 string str;
 int i;
 stringstream out1;
 stringstream out2;

 //Checks if sqrt(x) is an integer
 if(sqrt(x)-(int)sqrt(x) == 0)
    {
 //checks if x is palindrome

  out1 << x;
 str = out1.str();
 for(i=0;i<str.length()/2;i++)
 {
   if(str[i]!=str[str.length()-i-1]) return 0;
 }

 //checks if sqrt(x) is palindrome
  out2 << int(sqrt(x));
 str = out2.str();
 for(i=0;i<str.length()/2;i++)
 {
   if(str[i]!=str[str.length()-i-1]) return 0;
 }
 return 1;
    }
 else return 0;
}
