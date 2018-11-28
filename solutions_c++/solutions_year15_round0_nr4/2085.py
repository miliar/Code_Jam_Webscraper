#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int main(){
    
    ifstream in("D.in");
    ofstream out("D.out");
    
    int cases;
    in >> cases;
    
    for(int i=0;i<cases;i++){
            int x,r,c;
            
            in >> x >> r >> c;
            
            string won = "Gabriel";
            
            
            if(x == 2){
                 if((r*c) % 2 == 1) won = "Richard";
            }else if(x == 3){
                 if(r*c != 6 && r*c != 9 && r*c != 12) won = "Richard";    
            }else if(x ==4){
                  if(r*c!=12 && r*c!=16) won = "Richard";          
            }
            
            out << "Case #" << (i+1) << ": " << won << "\n";        
    }
}
