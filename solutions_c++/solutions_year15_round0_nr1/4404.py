#include <iostream>
#include <fstream>
using namespace std;

int main(){
    
    ifstream in("A-big.in");
    ofstream out("A.out");
    
    
    int cases;
    
    in>> cases;
    
    for(int i=0;i<cases;i++){
            int max, friends =0, total =0;
            in>>max;
            string people;
            in>>people;
            for(int j=0;j<=max;j++){
                    
                    int p = people[j] - '0';
                    
                    if(j>total){
                                friends+= (j - total);
                                total+= (j - total);            
                    }
                    total+=p;                                
            }        
            out << "Case #" << (i+1) << ": " << friends <<"\n";
    }


    //system("pause");
    
    
    
}
