#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

#define MAX(a,b) (((a)>(b))?(a):(b))

int main(int argc, char** argv) {

    ifstream infile("A-large.in");
    ofstream outfile("A-large.ou");

    int T;
    
    int S[10001];
    int sMax;

    infile >> T;
    
    for (int i = 0; i < T; i++) {
        infile >> sMax;
        int originalPeople = 0;
        int newPeople = 0;
        for (int j = 0; j <= sMax; j++) {
            char temp; 
            infile >> temp;
            S[j] = temp - '0';
            newPeople += MAX(0, (j - (originalPeople + newPeople)));
            originalPeople += S[j];
        }
        //cout << "Case #" << i + 1 << ": " << newPeople << endl;
        outfile << "Case #" << i + 1 << ": " << newPeople << endl;
        
    }
}

