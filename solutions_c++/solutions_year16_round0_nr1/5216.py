#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <string>

// Run as ./CountingSheep < input.txt

using namespace std;

void find_digs(bool *seen, int n) {
    do {
        int digit = n % 10;
        seen[digit] = true;
        n /= 10;
    } while (n > 0);
}

bool all_true(bool *seen) {
    for(int i=0;i<10;i++) {
        if ( !seen[i] ) { return false; }
    }
    return true;
}

int main(int argc, const char *argv[]) {
    
    int T, N;
    cin >> T;
	  	
    ofstream myfile;
    myfile.open ("output.txt");
    
    // Test cases
    for (int test = 0; test < T; test++) {
        
        // Read dimensions
        cin >> N;
        
        // Compute the number of counts
        bool seen[10];
        for(int i=0; i < 10; i++) { seen[i] = false; }
        int count = 0;
        int max_count = 100000;
        
        int kN = 0;
        while(!all_true(seen)) {
            kN += N;
            count++;
            find_digs(seen, kN);
            if (count > max_count) { count = max_count; break; }
        }
        
        // Print outcome
        if (count == max_count ) {
            myfile << "Case #" << (test + 1) << ": " << "INSOMNIA" << endl;
        }
        else {
            myfile << "Case #" << (test + 1) << ": " << kN << endl;
        }
    }
}