#include <iostream>
#include <math.h>
#include <stack>
#include <fstream>
using namespace std;
#include <string.h>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <conio.h>
#include <string>
#include <stdlib.h>
#include <stdio.h>

int main()
{
    ifstream file("in.in");
   ofstream out("out.out");
   string str;
   vector<long> l;
   long r=0;
   int n;
   int t=1;
   while(getline(file,str,'\n'))
   {
       int count[50];

       for(int k=0;k<str.length();k++)
       {   //cout<<"st "<<str[k]<<endl;
      // getch();
           if(str[k]==' ')
           {
              // cout<<r<<endl;
              // getch();
               l.push_back(r);
               r=0;
           }
           else
           {
               r=(10*r)+(static_cast<int>(str[k])-48);
              // cout<<"r="<<r<<endl;
               if(k==str.length()-1){l.push_back(r); r=0;}
           }
       }
