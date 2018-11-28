/*
	Alexandre Borgo - Google Code Jam - 2016 - C. Coin Jam
*/

#include <iostream>
#include <cmath>

using namespace std;

unsigned long long int fromBaseXtoBase10(int base, int length, int number[]) {
    unsigned long long int sum = 0;
    for(int i = 0 ; i < length ; i++) {
        sum += number[i]*pow(base,i);
    }
    return sum;
}

void displayNumber(int length, int number[]) {
    for(int i = length-1 ; i >= 0 ; i--) {
        cout << number[i];
    }
}

void generateNumber(int length, int number[], int index) {
    number[0] = 1;
    number[length-1] = 1;

    for(int i = 1 ; i <= length-2 ; i++) {
        if(index & 1) number[i] = 1;
        else number[i] = 0;
        index>>=1;
    }
}

bool isPrime(unsigned long long int number, unsigned long long int *divisor) {
    bool isPrime = true;

    for(unsigned long long int i = 2 ; i <= sqrt(number) ; i++) {

        if(number%i == 0) {
            isPrime = false;
            *divisor = i;
            break;
        }
    }    return isPrime;
}

int main() {
  int T;
  int n;
  int j;

  cin >> T;

  for(int i = 1 ; i <= T ; i++) {
    cin >> n;
    cin >> j;

    cout << "Case #" << i << ": " << endl;

    int index = 0;

    for(int c = 0 ; c < j ; c++) {

        int number[n];
        unsigned long long int baseConvert[9];
        unsigned long long int divisor[9];
        bool findJamcoin = false;

        do {
            findJamcoin = true;
            generateNumber(n,number,index);
            index++;

            for(int b = 2 ; b <= 10 ; b++) {
                baseConvert[b-2] = fromBaseXtoBase10(b,n,number);
                if(isPrime(baseConvert[b-2],&divisor[b-2])) findJamcoin = false;
            }
        } while(!findJamcoin);

        displayNumber(n,number);

        for(int b = 0 ; b < 9 ; b++) {
            cout << " " << divisor[b];
        }
        cout << endl;
    }
  }

  return 0;
}
