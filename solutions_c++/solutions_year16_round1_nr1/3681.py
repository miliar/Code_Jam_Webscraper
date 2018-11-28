#include <iostream>
#include <fstream>
#include <string>
#include <math.h>


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
    string word;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    
    for (int i=0; i<cases; ++i) {
        outfile << "Case #" << i+1 << ": ";
        int finished = 0;
        // read from file
        infile >> word;
        string lastword = "";
        int size = word.length();
        for (int j=0; j < size; ++j) {
            if (word[j]>=lastword[0]) lastword.insert(lastword.begin(),word[j]);
            else lastword.insert(lastword.end(),word[j]);
        }
        outfile << lastword << endl;
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
