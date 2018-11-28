// round12p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cassert>
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)


using namespace std;

bool ispalindrome(unsigned __int64  i)
{
   int digits[100];
   int numdigits = 0;
   int k;

   while (i>0)
   {
      digits[numdigits] = i %10;
      i = i/10;
     ++numdigits;
   }


   for (k=0;k<numdigits;++k)
   {
      if (digits[k]!=digits[numdigits-k-1]) return false; 
   }
   return true;

}



int main(int argc, char* argv[])
{
  int numCases;

  
  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
 	ifstream fin("C-large-1.in");FILE *f2 = fopen("C-large-1.out","w");
 //	ifstream fin("C-small-attempt0.in");FILE *f2 = fopen("C-small-attempt0.out","w");
  //	ifstream fin("C-small-attempt1.in");FILE *f2 = fopen("C-small-attempt1.out","w");
  //	ifstream fin("C-small-attempt2.in");FILE *f2 = fopen("C-small-attempt2.out","w");
  //	ifstream fin("C-small-attempt3.in");FILE *f2 = fopen("C-small-attempt3.out","w");
  

 
  unsigned __int64 i;
  set<unsigned __int64> palins;
  
  //Pre-Compute all the Fair and Square till 10^14
  for (i=0;i<=10000001;++i)
  {
    if (ispalindrome(i) && ispalindrome(i*i))  
    {
      palins.insert(i*i);
    }
  }
  
  char temp[20000];
  fin >> numCases;
  
  unsigned __int64 A;
  unsigned __int64 B;

  int counter;

  fin.getline(temp,20000);
  for (i=0;i<numCases;++i)
  {
  
   
    fin.getline(temp,20000);
    strstream ss,ss2;
    ss << temp;
    string str1,str2;
    ss >> str1;
    ss>> str2;

    A = 0;
    B = 0;

    while (str1.size() > 0)
    {
      int digit = (str1[0]-'0');
      str1 = str1.substr(1,str1.size()-1);
      A = (A*10+digit);
    }
    while (str2.size() > 0)
    {
      int digit = (str2[0]-'0');
      str2 = str2.substr(1,str2.size()-1);
      B = (B*10+digit);
    }
   
 

    counter = 0;
    std::set<unsigned __int64>::iterator mysi;
    for (mysi = palins.begin();mysi!=palins.end();++mysi)
    {
      unsigned __int64 temp = (*mysi);
      if ((temp >= A) && (temp <= B) ) ++counter;
    }
  

    fprintf(f2,"Case #%d: ",i+1);
    fprintf(f2,"%d\n",counter);

  }
    
    
    
 fclose(f2);   
  
 

 


  
  return 0;	
}