#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    ifstream input("a.in");
    ofstream output;
    output.open ("a.out");
    int T, mult;
    bool digits[10];
    input >> T;
    for(int i = 0; i < T; i++) {
        input >> mult;
        output << "Case #" << (i + 1) << ": ";
        if(mult){
            for(int j = 0; j < 10; j++) digits[j] = false;
            for(int j = 0; j < 100; j++) {
                int actual = (j + 1) * mult;
                for(int k = 1; k <= actual; k *= 10) {
                    digits[(actual % (k * 10)) / k] = true;
                }
                if(digits[0] && digits[1] && digits[2] && digits[3] && digits[4] && digits[5] && digits[6] &&
                   digits[7] && digits[8] && digits[9]) {
                    output << actual << "\n";
                    break;
                }
            }
        } else output << "INSOMNIA\n";
    }
    output.close();
    return 0;
}
