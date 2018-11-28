#include <iostream>
#include <cctype>
#include <algorithm>
#include <queue>
#include <string>
#include <stack>
#include <stdio.h>
#include <fstream>

using namespace std;

int main()
{
     ofstream oufile;
     ifstream infile;
     infile.open("A-small-attempt0.in");
    oufile.open ("output.out");
    int a,g1,g2;
    int array1[4][4],array2[4][4];
   infile>>a;
   for(int test=0;test<a;test++)
   {
   int counter=0;
   int temp=0;
    infile>>g1;
   for(int i=0;i<4;i++)
   for(int j=0;j<4;j++)
       infile>>array1[i][j];
       infile>>g2;
       for(int i=0;i<4;i++)
       for(int j=0;j<4;j++)
       infile>>array2[i][j];

       for(int i=0;i<4;i++)
       for(int j=0;j<4;j++)
       {
           if(array1[g1-1][i]==array2[g2-1][j])
           {
               counter++;
               temp=i;
           }

       }

       if (counter==0)
       oufile<< "Case #" << test+1<< ": " << "Volunteer cheated!"<< endl;
       else if (counter==1)
       oufile<< "Case #" << test+1<< ": " << array1[g1-1][temp]<< endl;
       else
        oufile<< "Case #" << test+1<< ": " << "Bad magician!"<< endl;



}
}
