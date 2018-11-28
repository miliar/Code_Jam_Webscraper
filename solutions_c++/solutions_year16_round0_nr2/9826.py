#include <iostream>
#include <fstream>
#include <string.h>
#include <map>
#include <vector>
#include <cmath>
#include <list>
#include <string>
#include <sstream>

using namespace std;

int getNumFlips(string &pancakes){
    int numflips = 0;
    unsigned int size = pancakes.size();
    char last = '+';
    for(int i=size-1; i>=0; i--){
        if(pancakes[i] != last){
            last = pancakes[i];
            numflips++;
        }
    }
    return numflips;
}

bool checkSleep(unsigned char buffer[]){
    for(int i=0; i<10; i++)
        if(buffer[i] == 0)
            return false;
    return true;
}

int main(int argc, char **argv){
    istream &in  = (argc>1)?*(new ifstream(argv[1])):cin;
    ostream &out = (argc>2)?*(new ofstream(argv[2])):cout;

    int T;
    in >> T;
    string b;
    getline(in, b); // just to remove \n from end of first line

    for(int i=1; i<=T; i++){

        string pancakes;
        getline(in, pancakes);
//        std::cout << "Reading " << pancakes << endl;

        out << "Case #" << i << ": " << getNumFlips(pancakes) << endl;

    }

    return 0;
}
