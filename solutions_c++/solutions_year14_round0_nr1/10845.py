// reading a text file
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <sstream>
using namespace std;


void test(int case_num, int num, int answer)
{
    cout <<"Case #"<<case_num<<": ";
    
    if (num == 0)
    {
        cout<<"Volunteer cheated!"<<endl;
    }
    else if (num ==1)
    {
        cout<<answer<<endl;   
    }
    else
    {
        cout<<"Bad magician!"<<endl;
    }    
}



int main () {
  string line;
  int firstRow = 0;
   int secondRow = 0;
  vector<int> rowsA;  
  vector<int> rowsB;
  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {
    getline(myfile,line);
    int cases =atoi(line.c_str());    
    
    for (int number = 1; number<=cases;number++)
    {
        getline(myfile,line);
        firstRow =atoi(line.c_str());
        
        for (int i = 1; i<=4;i++)
        {
            getline(myfile,line);
            if (firstRow == i)
            {
                int numbers =0;
                std::istringstream iss(line);

                while(iss >> numbers) //Extract integers from line
                    {
                        rowsA.push_back(numbers);
                    }
                
                for (int j=0; j<rowsA.size();j++)
                {
                   // cout<< rowsA.at(j)<<": Row A"<<endl;
                    
                }
                
                
            }
            
        }
         getline(myfile,line);
        secondRow =atoi(line.c_str());
        
          for (int i = 1; i<=4;i++)
        {
            getline(myfile,line);
            if (secondRow == i)
            {
                int numbers =0;
                std::istringstream iss(line);

                while(iss >> numbers) //Extract integers from line
                    {
                        rowsB.push_back(numbers);
                    }
                
              
                
                for (int j=0; j<rowsB.size();j++)
                {
                    //cout<< rowsB.at(j)<<": RowB"<<endl;
                    
                }
               
               
               
               
            }
            
        }
        
        int counter = 0;
        int answer = 0;
         for (int j=0; j<rowsA.size();j++)
        {
                      
                
                 for (int k=0; k<rowsB.size();k++)
                {
                    if (rowsA.at(j) == rowsB.at(k))
                    {
                        counter++;
                        answer = rowsB.at(k);
                    }                    
                }
                
                
                
                
                    
        }
        test(number,counter, answer);
        
        //COMPARE VECTORS
        
        
        
        rowsA.clear();
        rowsB.clear();
        
    }  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    /*  
    while ( getline (myfile,line) )
    {
      cout << line << '\n';
      
    }*/
    
    
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}



