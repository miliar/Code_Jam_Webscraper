#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>
#include<fstream>
using namespace std;

#define f(i,n) for(i=0;i<n;i++)
#define f1(i,n) for(i=1;i<n;i++)
#define takeinp(inp,fptr) fptr>>inp


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int test,t,i,j,n;

    ifstream myinpfile;
    ofstream myoutfile;
    myinpfile.open("i9.in");
    myoutfile.open("out1.txt");
    takeinp(test,myinpfile);
    f(i,test)
        {
            takeinp(n,myinpfile);
            int * inp= new int [n];
            int count =0;
           f(j,n)
           {
               takeinp(inp[j],myinpfile);
           }
           int last=inp[0];
           f1(j,n)
           {
               if(inp[j]<last)
               {
                   count+=last-inp[j];


               }
               last=inp[j];
           }
           // max rate
           int lmax=inp[0]-inp[1];
           for(j=2;j<n;j++)
           {
               int temp=inp[j-1]-inp[j];
               if(temp>lmax)
               lmax=temp;

           }
           int count1=0;
           for(j=0;j<n-1;j++)
           {
               if(inp[j]>lmax)
               count1+=lmax;
               else
               count1+=inp[j];

           }


            myoutfile<<"Case #"<<i+1<<": "<<count<<" "<<count1<<" "<<endl;

        }
		myinpfile.close();
		myoutfile.close();


    return 0;
}
