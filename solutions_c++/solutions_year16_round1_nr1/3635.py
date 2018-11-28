#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main(){
    string line;
    string wordcase [100];
    int maxcase = 0;
    int i = 0;
    
   ifstream myfile ("A-large.in");
    if (myfile.is_open())
    {  
       getline(myfile, line);
       stringstream(line) >> maxcase;
       for (i = 0; i < maxcase; i++){
           getline(myfile, wordcase[i]);    
       }
       myfile.close();
    }//else cout << "Unable to open file"; 
    
    int j = 0;
    char c, c1, clast;
    string check;
    for (i = 0; i < maxcase; i++){
        j = 0;
        check = "";
        
        while (j < wordcase[i].size()){
              c = wordcase[i][j];
              if (check.size() <= 0)
                 check = check + c;
              else {
                   c1 = check[0];
                   clast = check[check.size()-1];
                   
                   if (c >= c1)
                      check = c + check;
                   else 
                        check = check + c;                   
              } //else if check
              ++j;
        } // end j
        
        wordcase[i] = check;
    } // end i
    
    
  ofstream myfileo ("output2.txt");
  if (myfileo.is_open())
  {
     for (i = 0; i < maxcase; i++){
         myfileo << "Case #" << i+1 << ": ";
         myfileo << wordcase[i] << '\n';
    }
    myfileo.close();
  }//else cout << "Unable to open file";
  
    return 0;
}//end main
