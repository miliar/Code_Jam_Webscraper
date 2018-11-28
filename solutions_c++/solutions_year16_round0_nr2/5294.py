#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <string>

// Run as ./FlippingPancakes < input.txt

using namespace std;

// Flip the first k elements
void flip(std::vector<bool> &vec, int k) {
    bool temp[k];
    for(int i=0; i<k; i++) {
        temp[i] = !vec[k-1-i];
    }
    for(int i=0;i<k;i++) {
        vec[i] = temp[i];
    }
}

// Returns -1 if we are done
int findk(std::vector<bool> orientation) {
    int o = orientation[0];
    int k=1;
    for(int i=1; i<orientation.size(); i++) {
        if (orientation[i] != o) { k = i; break; }
        if (i == orientation.size()-1) { k = orientation.size(); }
    }
    // Check if we are done
    if (o && k == orientation.size()) {
        return -1;
    }
    return k;
}

int main(int argc, const char *argv[]) {
    
    int T;
    string N;
    cin >> T;
	  	
    ofstream myfile;
    myfile.open ("output.txt");
    
    // Test cases
    std::cout << T << std::endl;
    for (int test = 0; test < T; test++) {
        std::vector<bool> orientation;
        
        // Read orientation
        cin >> N;
        for(int i=0; i < N.size();i++) {
            if(N[i] == '+') {
                orientation.push_back(true);
            }
            else if(N[i] == '-') {
                orientation.push_back(false);
            }
        }
        
        // Keep flipping the first k until we are done
        int k = findk(orientation);
        int count = 0;
        while(k != -1) {
            flip(orientation, k);
            count++;
            k = findk(orientation);
        }
            
        // Print outcome
        myfile << "Case #" << (test + 1) << ": " << count << endl;
    }
}