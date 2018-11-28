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
    ifstream myfile("a-large.in.txt");
    
    ofstream outputfile("output.txt");
    if (myfile.is_open())
    {   getline (myfile,line);
        stringstream num_cases(line);
        num_cases>>cases;

    
        for(int i=0;i<cases; i++)
        {
            getline(myfile,line);
            stringstream input(line);
            int number;
            input>>number;
            if (number==0)
            {
                outputfile<< "Case #";
                outputfile<<i+1;
                outputfile<<": ";
                outputfile<<"INSOMNIA";
                outputfile<<"\n";
                
            }
            else
            {
                int result=number;
                vector<bool> seen(10,false);
                while(finish(seen)==false)
                {
                    int remaining=result;
                    
                    
                    while(remaining>0){
                        seen[remaining%10]=true;
                        remaining=remaining/10;
                        
                    }
                    
                    result=result+number;
                    
                }
                outputfile<< "Case #";
                outputfile<<i+1;
                outputfile<<": ";
                outputfile<<result-number;
                outputfile<<"\n";
            
            }
            
            
                
            
           
          
          
          
            
        }
        
  
        
        myfile.close();
    }
    
}
