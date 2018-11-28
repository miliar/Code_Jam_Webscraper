#include<iostream>
#include<stdio.h>
#include<string>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main()
{ int t,k,i,sum,f,d,s;

 string str;

 ifstream pFile ("A-large.in");
 {

  ofstream fo("ANSFILE0.txt");

pFile>>t;


 i=1;
 while( i <= t )
 {  s=0;
    str="";
    sum=0;
    f=0;
    k=0;
    d=0;

    pFile>>s>>str;

    while(k < str.length())
     {

        if( sum < k )
          {
              d = k-sum;
              f += d;
              sum+=d;

          }

       sum +=str[k]-48;
        k++;
     }

     fo<<"Case #"<<i<<": "<<f<<"\n";

     i++;
  }

}

  return 0;
}
