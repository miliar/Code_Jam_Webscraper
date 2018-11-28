//
//  main.cpp
//  Playground
//


#include <iostream>
#include <fstream>
#include<sstream>
#include <string>
#include <vector>

#include <cmath>
#include <math.h>
using namespace std;
bool finish(vector<bool> seen)
{
    bool result =true;
    for (int i = 0;i<10;i++)
    {
        if(seen[i]==false)
        {
            result=false;
        }
    }
    return result;
}

int main() {

    int cases;

    string line="cccc";
    ifstream myfile("c-small-attempt0.in.txt");
    
    ofstream outputfile("output.txt");
    if (myfile.is_open())
    {   getline (myfile,line);
        stringstream num_cases(line);
        num_cases>>cases;

    
        for(int i=0;i<cases; i++)
        {
            getline(myfile,line);
            stringstream input(line);
            string str;
            input>>str;
            int result=0;
            if(*str.begin()=='-')
            {
                result+=1;
            }
            for (string::iterator it=str.begin()+1;it!=str.end();it++)
            {
                if(*(it-1)=='+'&&*it=='-')
                {
                    result+=2;
                }
            }
         
            outputfile<< "Case #";
            outputfile<<i+1;
            outputfile<<": ";
            outputfile<<"\n";
            for (int j=0;j<16;j++)
            {
                 outputfile<<"1";
            }
            for(int j=2; j<11;j++)
            {
                outputfile<<" ";
                outputfile << j+1;
                
            }
            
        
            outputfile<<"\n";
            for(int i=0; i<49;i++)
            {
                outputfile<<"1";
                for (int j=15;j>1;j--)
                {
                    if (i%7*2==j%14||i/7*2+1==j%14)
                    {
                        outputfile<<"1";
                    }
                    else
                    {
                        outputfile<<"0";
                    }
                }
                outputfile<<"1";
                for(int j=2; j<11;j++)
                {
                    outputfile<<" ";
                    outputfile << j+1;
                    
                }
                outputfile<<"\n";
                
            }
            
            
            
                
            
           
          
          
          
            
        }
        
  
        
        myfile.close();
    }
    
}
