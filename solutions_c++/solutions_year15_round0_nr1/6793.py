#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <fstream>

using namespace std;

ifstream iFile("input.in");
ofstream oFile("output.txt");
int standing;

int main() {
    int T;
    iFile >> T;

    for (int t=1; t <= T; t++) {
        standing = 0;
        int Smax;
        int total = 0;
        int friends = 0;
        char c;
        iFile >> Smax;
        int* audience = new int[Smax + 1];
        for (int i=0; i <= Smax; i++) {
            iFile >> c;
            audience[i] = c - '0';
            total += audience[i];
        }

        for (int i=0; i <= Smax; i++) {
            if (standing <= i) {
                int dif = i - standing;
                friends += dif;
                standing += dif;
            }
            standing += audience[i];
        }

        oFile << "Case #" << t << ": " << friends << endl;
    }
}
