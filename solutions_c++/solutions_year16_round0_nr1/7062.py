#include <stdlib.h>
#include <array>
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
#include <fstream>

using namespace std;

string solve(uint64_t N) {
    int count = 0;
    array<bool, 10> digits;
    digits.fill(false);

    bool can_find = true;
    int i = 0;
    
    if (N == 0) {
        can_find = false;
    }

    while(count < 10 && can_find){
        i++;
        uint64_t cn = i * N;

        while(cn > 0){
            int d = cn % 10;
            cn = cn / 10;
            digits[d] = true;
        }

        count = 0;
        for(auto& q: digits) {
            if (q) {
                count++;
            }
        }
    }

    if (count == 10) {
        return to_string(i * N);
    } else {
        return "INSOMNIA";
    }
}

int main(){
    ifstream inf;
    inf.open("A-large.in");
    ofstream ouf;
    ouf.open("1.out");
    int T;
    inf >> T;
    for(int i = 0; i < T; ++i) {
        uint64_t N;
        inf >> N;
        ouf << "Case #" << i + 1 << ": " << solve(N) << endl;
    }
    ouf.close();
    inf.close();
}
