#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
    int T;
    int i, j;
    int Smax;
    
    int currentlyClapping, necessaryAdditions;
    
    ifstream testFile("a.in");
    freopen("a.out", "w", stdout);
    
    testFile >> T;
    
    for(i = 0; i < T; i++) {
        currentlyClapping = 0;
        necessaryAdditions = 0;
        
        testFile >> Smax;
        testFile.get();

        for(j = 0; (j < (Smax + 1)); j++) {
            int value = (testFile.get() - '0');
            if(value > 0) {
                if(j > currentlyClapping) {
                    necessaryAdditions += (j - currentlyClapping);
                    currentlyClapping += necessaryAdditions;
                    currentlyClapping += value;
                } else {
                    currentlyClapping += value;
                }               
            }
        }
        
        cout << "Case #" << i+1 << ": " << necessaryAdditions << "\n";
    }
    
    return 0;
}

