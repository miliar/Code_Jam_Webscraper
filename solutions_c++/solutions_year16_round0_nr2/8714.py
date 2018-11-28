#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;


int main(){
    string line;
    string pancakes [100];
    int maxcase = 0;
    int i = 0;
    
    ifstream myfile ("B-large.in");
    if (myfile.is_open())
    {  
       getline(myfile, line);
       stringstream(line) >> maxcase;
       for (i = 0; i < maxcase; i++){
           getline(myfile, pancakes[i]);    
       }
       myfile.close();
    }//else cout << "Unable to open file"; 
    
    /* MAIN */
    int tries [100];
    int j, pansize;
    char c, side;
    
    for (i = 0; i < 100; i++)              //initialize
        tries[i] = 0;
        
    for (i = 0; i < maxcase; i++){
        pansize = pancakes[i].size();
        side = pancakes[i][pansize-1]; 
        if (side == '-'){
           tries[i]++;
           side = '-';
        }
        pansize--;       
        while (pansize > 0){
              c = pancakes[i][pansize-1];
              if (c != side){
                 tries[i]++;
                 side = c;   
              }//if c
              --pansize;
        }//while pansize        
    }//for i
  
  ofstream myfileo ("output2.txt");
  if (myfileo.is_open())
  {
     for (i = 0; i < maxcase; i++){
         myfileo << "Case #" << i+1 << ": ";
         myfileo << tries[i] << '\n';
    }
    myfileo.close();
  }//else cout << "Unable to open file";


   // system("pause");
    return 0;
}//end of main
