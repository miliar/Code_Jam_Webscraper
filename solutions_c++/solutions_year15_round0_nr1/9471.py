#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <ctype.h>
#include <sstream>
#include <fstream>
using namespace std;

// Driver program to test above functions
int main() {
    string file_path = "/Users/aidan/Desktop/jam/input.in";
    ifstream data (file_path.c_str(), ios::in);
    ofstream ret ("/Users/aidan/Desktop/jam/output.out");
    int T, SMAX;
    data >> T;
    
    for (int round = 1; round <= T; round++) {
        data >> SMAX;
        string A = "";
        data >> A;
        
        if (A.size() != SMAX + 1)
            cout << "Wrong!!!" << endl;
        
        int total = 0, need = 0;
        
        for (int i = 0; i <= SMAX; i++) {
            // if current total standing people is smaller than index i
            // we need to borrow (i - total) people to make A[i] stand up
            if (total < i) {
                need += i - total;
                total = i;
            }
            total += A[i] - '0';
        }
        
        ret << "Case #" << round << ": " << need << endl;
    }
    ret.close();
    return 0;
}


