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
     ofstream myfile;
     ifstream infile;
     infile.open("input.in");
    myfile.open ("output.out");
    int n,guess1,guess2;
    int arr1[4][4],arr2[4][4];
   infile>>n;
   for(int test=0;test<n;test++)
   {
   int counter=0;
   int temp=0;
    infile>>guess1;
   for(int i=0;i<4;i++)
   for(int j=0;j<4;j++)
       infile>>arr1[i][j];
       infile>>guess2;
       for(int i=0;i<4;i++)
       for(int j=0;j<4;j++)
       infile>>arr2[i][j];

       for(int i=0;i<4;i++)
       for(int j=0;j<4;j++)
       {
           if(arr1[guess1-1][i]==arr2[guess2-1][j])
           {
               counter++;
               temp=i;
           }

       }

       if (counter==0)
       myfile<< "Case #" << test+1<< ": " << "Volunteer cheated!"<< endl;
       else if (counter==1)
       myfile<< "Case #" << test+1<< ": " << arr1[guess1-1][temp]<< endl;
       else
        myfile<< "Case #" << test+1<< ": " << "Bad magician!"<< endl;



}
}
