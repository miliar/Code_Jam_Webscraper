#include <iostream>
#include <fstream>
#include <string>
#include <stdint.h>

using namespace std;

int main(){
    ifstream input("d.in");
    ofstream output;
    output.open ("d.out");
    unsigned long long T, K, C, S;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        unsigned long long pos, pow, plus;
        input >> K >> C >> S;
        output << "Case #" << (i + 1) << ":";
        pow = 1;
        for(unsigned int j = 0; j < C - 1; j++) pow *= K;
        for(unsigned int j = 0; j < K; j++) {
            pos = j * pow;
            plus = 1;
            for(unsigned int k = 1; k < C; k++) {
                pos += j * plus;
                plus *= K;
            }
            output << " " << (pos + 1);
        }
        output << endl;
    }
    output.close();
    return 0;
}
