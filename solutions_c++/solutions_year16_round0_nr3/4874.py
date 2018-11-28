#include <iostream>
#include <math.h>

using namespace std;

long long unsigned int convertToBase(string n, int base) {
    long long unsigned int ret = 0;

    for (int cont = 15; cont >= 0; cont--) {
        if (n[cont] == '1') {
            ret += pow(base, 15 - cont);
        }


    }

    return ret;
}

long long unsigned int smallestDivisor(long long unsigned int n) {
    if (n % 2 == 0) {
        return n;
    }

    for (long long unsigned int i = 3; i<sqrt(n); i += 2) {
        if(n % i == 0) return i;
    }
    return n;
}

void makeAllBinaryNumbers(string a[]) {
    a[0] = "1000000000000001";

    int cont = 0;
    for (int i = 1; i < 16384; i *= 2) {

        for (int j = 0; j <= i; j++) {
            a[i + j] = a[j];
            a[i + j][14 - cont] = '1';

        }

        cont++;
    }
}

int main() {
    std::ios::sync_with_stdio(false);

    string possibleJamCoins[16385]; //That is how many 16bits binary numbers with 1...1 there are
    makeAllBinaryNumbers(possibleJamCoins);

    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++) {
        int n, j;

        cin >> n >> j;

        cout << "Case #" << i << ":" << endl;

        int lastJamCoin = -1;
        for (int k = 0; k < j; k++) {
            string toPrint = "";

            for (int l = lastJamCoin + 1; l < 16384; l++) {
                int m = 2;
                toPrint = "";
                for (m = 2; m <= 10; m++) {
                    long long unsigned int converted = convertToBase(possibleJamCoins[l], m);
                    long long unsigned int divisor = smallestDivisor(converted);
                    if (converted == divisor) break;
                    else toPrint += " " + to_string(divisor);
                }

                if(m==11) {
                    lastJamCoin = l;
                    break;
                }
            }

            cout << possibleJamCoins[lastJamCoin] << toPrint << endl;

        }
    }

    return 0;
}
