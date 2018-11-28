#include<iostream>
#include<fstream>
#include<math.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int palindrome(int x)
{  int i;
  char s[100]=""; sprintf(s,"%d",x);
   for(i=0;i<strlen(s)/2;i++)
    {if(s[i]!=s[strlen(s)-i-1]) return 0;}
  return 1;
}
int main()
{
   ifstream fin; fin.open("input");
  ofstream fout;  fout.open("output");
   int nt; fin>>nt; 
     int k;
    for(k=1;k<=nt;k++)
      {
          char A[100],B[100]; fin>>A>>B;
           long long a,b,palcount=0; a=ceil(sqrt(atof(A)));
               b=floor(sqrt(atof(B))); 
          for(;a<=b;a++)
          {
             if(palindrome(a)) {if(palindrome(int(pow(a,2)))) palcount++;}
          }
            fout<<"Case #"<<k<<": "<<palcount<<"\n";
      }
}
