#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <bitset>

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
    int K;
    int C;
    int S;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    
    for (int i=0; i<cases; ++i) {
        outfile << "Case #" << i+1 << ": ";
        int finished = 0;
        // read from file
        infile >> K;
        infile >> C;
        infile >> S;
        int clean = 1;
        for (int j=0;j<K; j++) {
            //clean = 1+j*pow(K,C-1);
            outfile << clean;
            clean++;
            if (j==K-1) outfile << endl;
            else outfile << " ";
        }
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
