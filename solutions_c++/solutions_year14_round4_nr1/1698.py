//
//  Q1.cc
//  
//
//
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Need input file!" << endl;
        return 1;
    }
    ifstream input(argv[1]); // bind and open the input file
    // check whether open sucessfully
    if (!input) {
        cerr << "unable to open the input file!" << endl;
        return 1;
    }
    
    int T; // number of cases
    input >> T;
    input.ignore(256, '\n'); // ignore the rest of the line
    
    // consider each case
    for (int t = 1; t <= T; t++) {
        int N, X; // number, size
        input >> N >> X;
        input.ignore(256, '\n'); //ignore the rest of the line
        // get each size
        vector<bool> visited(N, false);
        vector<int> sizes(N, 0);
        for (int i = 0; i < N; i++) input >> sizes[i];
        input.ignore(256, '\n'); //ignore the rest of the line
        // sort the sizes
        sort(sizes.begin(), sizes.end());
        int numDisks = 0;
        for (int i = 0; i < N; i++) {
            if (visited[i]) continue;
            // visit this file
            visited[i] = true;
            numDisks++;
            // binary search
            int lo = i+1;
            int hi = N-1;
            double target = X - sizes[i] + 0.1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (sizes[mid] < target) lo = mid+1;
                else hi = mid-1;
            }
            while (hi > i && visited[hi]) hi--;
            if (hi > i && !visited[hi]) visited[hi] = true;
        }
        
        cout << "Case #" << t << ": " << numDisks << endl;
        
    }
    
    input.close(); // close file before return
    
    return 0;
}
