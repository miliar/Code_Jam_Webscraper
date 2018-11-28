
#include <algorithm>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <stdio.h>
#include <utility>
#include <iomanip>
#include <set>
#include <map>
#include <fstream>
#include<iostream>
using namespace std;

int main()
{


     ofstream myfile;
      ifstream infile;
      infile.open("input.in");
     myfile.open ("out.out");
    int test;
     infile>>test;
      for(int z=0;z<test;z++)
      {
            int a,b,k;
            infile>>a;
            infile>>b;
            infile>>k;
            int count =0;

            for(int i=0;i<a;i++)
            {
                for(int j=0;j<b;j++)
               {
                   int x=i &j;
                if(x<k)
                count++;
               }
            }
        myfile<< "Case #"<<z+1<<": " << count<<endl;
        }
}
