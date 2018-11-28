#include <iostream>
#include <fstream>
#include <string>
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
    string stack;
    
    for (int i=0; i<cases; ++i) {
        // read from file
        infile >> stack;
        //cout << stack << endl ;
        int size = stack.size();
        //cout << size << endl ;
        int swaps=0;
        
        // algorithm
        for (int j=size-1; j>=0; --j) {
            //cout << stack << endl ;
            if (stack[j]=='+') {
            } else {
                swaps++;
                for (int k=j; k>=0; k-- ){
                    if (stack[k]=='+') stack[k]='-';
                    else stack[k]='+';
                }
                //cout <<"Swaped:"<< stack << endl ;
            }
        }
        outfile << "Case #" << i+1 << ": ";
        outfile << swaps << endl;
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
