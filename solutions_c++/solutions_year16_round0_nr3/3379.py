#include <queue>
#include <string>
#include <iostream>
#include <vector>
#include <bitset>
#include <tgmath.h>

using namespace std;

int main() {
    int trash, N, J;
    cin >> trash;
    cin >> N;
    cin >> J;
    int inner = N-2;
    int range = (int) pow(2, inner);
    int count = 0;
    char buffer[N+1];
    queue<long> factors;
    cout << "Case #1:" << endl;
    for (int in=0; in<range; in++) {
        // flag
        bitset<14> I(in);
        string bit_string = "1" + I.to_string() + "1";
        //cout << bit_string << endl;
        while (!factors.empty()) {
            factors.pop();
        }
        
        bool ok = true;
        for (int base=2; base<=10; base++) {
            long value = 0;
            for (int index=0; index<bit_string.length(); index++) {
                long ind;
                if (bit_string[index] == '1') {
                    ind = 1;
                } else {
                    ind = 0;
                }
                value += ind * (long) pow(base, bit_string.length()-1-index);
            }
            //cout << value << endl;
            bool good = false;
            for (long fac=3; fac<10000; fac++) {
                if (value % fac == 0) {
                    //cout << "VALUE: " << fac << endl;
                    good = true;
                    factors.push(fac);
                    break;
                }
            }
            if (!good) {
                ok = false;
                break;
            }
        }

        if (ok) {
            cout << bit_string << " ";
            while (!factors.empty()) {
                cout << factors.front() << " ";
                factors.pop();
            }
            cout << endl;
            count++;
        }
        if (count == 50) {
            return 0;
        }
    }
}
