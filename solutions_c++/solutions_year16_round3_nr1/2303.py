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
bool pairCompare(const std::pair<int, unsigned long>& firstElem, const pair<int, unsigned long>& secondElem) {
    return firstElem.first < secondElem.first;
    
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
            int numbers;
            input>>numbers;
            vector<int> members(numbers);
            int sum=0;
            getline(myfile,line);
            stringstream inputt(line);
            for (int j=0; j<numbers;j++)
            {
                
               
                inputt>>members[j];
                sum+=members[j];
            }
            vector<pair<int,unsigned long>> idxmember(numbers);
            for(int j=0;j<numbers;j++)
            {
                idxmember[j]=make_pair(members[j],j);
            }
            sort(idxmember.begin(), idxmember.end(),pairCompare);
            
            outputfile<< "Case #";
            outputfile<<i+1;
            outputfile<<": ";
            if(sum%2==0)
            {
                for (int k=0; k<sum/2;k++)
                {
                    sort(idxmember.begin(), idxmember.end(),pairCompare);
                    outputfile<<static_cast<char> (idxmember[idxmember.size()-1].second+65);
                    idxmember[idxmember.size()-1].first-=1;
                    
                    sort(idxmember.begin(), idxmember.end(),pairCompare);
                    outputfile<<static_cast<char> (idxmember[idxmember.size()-1].second+65);
                    idxmember[idxmember.size()-1].first-=1;

                    outputfile<<" ";

                }
                
                
                
            }
            if(sum%2!=0)
            {
                sort(idxmember.begin(), idxmember.end(),pairCompare);
                outputfile<<static_cast<char> (idxmember[idxmember.size()-1].second+65);
                idxmember[idxmember.size()-1].first-=1;

                outputfile<<" ";
                
                for (int k=0; k<(sum-1)/2;k++)
                {
                    
                    sort(idxmember.begin(), idxmember.end(),pairCompare);
                    outputfile<<static_cast<char> (idxmember[idxmember.size()-1].second+65);
                    idxmember[idxmember.size()-1].first-=1;
                    
                    sort(idxmember.begin(), idxmember.end(),pairCompare);
                    outputfile<<static_cast<char> (idxmember[idxmember.size()-1].second+65);
                    idxmember[idxmember.size()-1].first-=1;


                    outputfile<<" ";
                    
                }
                
                
                
            }

          
            outputfile<<"\n";

     
              

                
            
            
          
         
            
            
                
            
           
          
          
          
            
        }
        
  
        
        myfile.close();
    }
    
}
