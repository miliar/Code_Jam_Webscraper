
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <stack>
#include <map>
#include <vector>
using namespace std;
typedef long long int lli;


int main() {
    
    ifstream fin ("input.txt");
    ofstream fout ("ans.txt");
    
    lli T; fin >> T;
    for (lli t = 0; t < T; t++) {
    
        fout << "Case #" << t+1 << ":";
        
        int K, C, S; fin >> K >> C >> S;
        for (int i = 1; i <= K; i++) {
            fout << " " << i;
        }
        fout << "\n";
    }
    
    return 0;
}