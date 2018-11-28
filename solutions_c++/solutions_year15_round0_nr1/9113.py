/* 
 * File:   main.cpp
 * Author: islam
 *
 * Created on April 11, 2015, 5:33 PM
 */

#include <fstream>
#include <string>

using namespace std;
int testCases;

int main(int argc, char** argv) {
    ifstream ins("input.in");
    ofstream outs("output.out");
    ins >> testCases;
    for (int caseCount = 1; caseCount <= testCases; caseCount++) {
        int maxShyness;
        string shyness;
        ins >> maxShyness;
        ins >> shyness;
        int sol = 0;
        int cheering = 0;
        for (int i = 0; i < shyness.size(); i++) {
            int currCount = int(shyness.at(i) - '0');
            int need = i - cheering;
            if (need > 0) {
                sol += need;
                cheering += need;
            }
            cheering += currCount;
        }
        outs << "Case #" << caseCount << ": " << sol << endl;
    }
    return 0;
}

