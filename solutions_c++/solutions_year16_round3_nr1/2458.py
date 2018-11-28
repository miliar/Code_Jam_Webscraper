#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;


int main (int argc, char* args[]){
    ifstream infile;
    ofstream outfile;
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        infile.open("small.in");
        outfile.open("small.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        infile.open("large.in");
        outfile.open("large.out");
    }
    
    int cases;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    
    for (int i=0; i<cases; ++i) {
        outfile << "Case #" << i+1 << ": ";
        //cout << "Case #" << i+1 << ": " << endl;
        //int finished = 0;
        // read from file
        int numparties;
        int parties[26]={};
        infile >> numparties;
        
        for (int j=0; j<numparties; ++j) {
            infile >> parties[j];
        }
        
        //int max_test =
        int max_ele = * max_element(parties,parties+numparties);
        int max_num = 0;
        
        while(*max_element(parties,parties+numparties) != 0){
            
            max_ele = *max_element(parties,parties+numparties);
            max_num = 0;
            
            for (int j=0; j<numparties; ++j) {
                if (parties[j]==max_ele) max_num++;
            }
            //cout << max_num << endl;
            if (max_num%2 == 1){
                for (int j=0; j<numparties; ++j) {
                    if (parties[j]==max_ele){
                        parties[j]--;
                        outfile<< char('A' + j) << " ";
                        break;
                    }
                }
            }
            else if (max_num%2 == 0){
                int count=0;
                for (int j=0; j<numparties; ++j) {
                    if (parties[j]==max_ele){
                        parties[j]--;
                        outfile<< char('A' + j);
                        count++;
                        if(count == 2){
                            outfile<< " ";
                            break;
                        }
                    }
                }
            }
            else cout<< "ERROR";
            
        }
        outfile<< endl;
        
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
