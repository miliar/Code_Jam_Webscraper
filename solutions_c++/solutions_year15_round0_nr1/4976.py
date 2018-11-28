#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>

using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int T, smax;
    cin >> T;
    ofstream myfile;
    myfile.open ("ovation.txt");
    for (int i = 0; i < T; i++) {
        cin >> smax;
        int standing, added;
        string input;
        standing = added = 0;
        cin >> input;
        int it = 0;
        for(char& d : input) {
            if (static_cast<int>(d - '0') != 0) { 
                if (standing > it) {
                    standing += static_cast<int>(d - '0');
                } else {
                    added += (it - standing);
                    standing += static_cast<int>(d - '0') + added;
                }
            }
            ++it;
        }
        myfile << "Case #" << i+1 << ": " << added << endl;
    }
    myfile.close();
    return 0;
}
