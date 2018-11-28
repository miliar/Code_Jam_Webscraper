#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
using namespace std;



int main() {
    //    freopen("input.txt", "rt", stdin);
    //    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    
    for (int i = 1; i <= T; i++) {
        string S;
        cin >> S;
        
        char cur = S[0];
        int countFlips = 0;
        
        for (int j = 1; j < S.size(); j++) {
            if (S[j] != cur) {
                countFlips += 1;
                cur = S[j];
            }
        }
        
        if (S[S.size()-1] == '-')
            countFlips++;

        cout << "Case #" << i << ": " << countFlips << endl;
    }
    
}

