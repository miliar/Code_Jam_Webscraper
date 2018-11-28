#include <utility>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <cstdlib>
#include <string.h>
#include <fstream>
#include <climits>
#include <vector>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;



int main() {
//    ifstream ifs("/Users/Raffaele/Desktop/CodeJam/2014/1b/2/small.in");
//    ofstream ofs("/Users/Raffaele/Desktop/CodeJam/2014/1b/2/small.out");
//    cin.rdbuf(ifs.rdbuf());
//    cout.rdbuf(ofs.rdbuf());
    
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        int A, B, K, res = 0;
        cin >> A >> B >> K;
        for (int i = 0; i < A; i++) {
            for (int j = 0; j < B; j++) {
                if ((i & j) < K) res++;
            }
        }
        cout << "Case #" << test << ": " << res << endl;
    }
    
    return 0;
}



