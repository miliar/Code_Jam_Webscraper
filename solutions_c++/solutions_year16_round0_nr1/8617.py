#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main(){
    long long ncase [100];
    bool n[10];
    int i = 0;
    int maxcase = 0;
    string line;
    
    //input file
    ifstream myfile ("A-large.in");
    if (myfile.is_open()){
                          
       getline(myfile, line);
       stringstream(line) >> maxcase;
       
       while (i < maxcase){
             getline (myfile, line);            
             stringstream(line) >> ncase[i];
             ++i;
       }
       myfile.close();
    }// else cout << "Unable to open file"; 
    
    
    /* MAIN */    
    string check;
    int j, k, l;
    char c;
    int counter = 0, nextnum = 0;
    
    for (i = 0; i < maxcase; i++){           
        for (j = 0; j< 10; j++)          //clear bool
            n[j] = false;
        
        counter = 0;    
        l = 1;    
        
        while ((ncase[i] > 0) && (counter < 10)){
           nextnum = ncase[i]*l;
           stringstream ss;
           ss << nextnum;
           check = "";
           check = ss.str();  
           k = check.size();          
           while (k > 0){
                 j = 0;
                 c = check[k-1];
                 while ((j < 10) && (counter < 10)){
                    if (!n[j]){                                       
                       if ((static_cast<int>(c)-48) == j){
                          n[j] = true;
                          counter++;
                          j = 10;
                       }
                    }
                    ++j;
                 }
                 --k;                    
           }
           ++l;               
        } 
        
        if (counter == 0) 
           ncase[i] = 0;  
        else 
            ncase[i] = ncase[i] * (l-1);     
    }
    
  ofstream myfileo ("output2.txt");
  if (myfileo.is_open())
  {
    for (i = 0; i < maxcase; i++){
        myfileo << "Case #" << i+1 << ": ";
        if (ncase[i] == 0)
           myfileo << "INSOMNIA";
        else 
             myfileo << ncase[i];
        myfileo << '\n';
    }
    myfileo.close();
  }//else cout << "Unable to open file";

    return 0;   
}
