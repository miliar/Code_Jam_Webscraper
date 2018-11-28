#include <iostream>
#include <cmath>
#include <string>
using namespace std;

bool is_prime(unsigned long, int&);
unsigned long convert_to_base(unsigned int, int , int);
string Convert(unsigned int);
bool is_jamcoin(unsigned int, int ,int []);
int main() {
    int cases, N, J;
    cin >> cases;
    cin >> N;
    cin >> J;
    cout << "Case #" << 1 << ":\n";
    unsigned int count = 0;
    unsigned int number = 0 | int(pow(2, N-1)) + 1;
    int divisors [11];
    for (int i = 0; i < int(pow(2, N-2)); ++i) {
        if (count == J) break;
        unsigned int jamcoin = number | (i << 1);
        if (is_jamcoin(jamcoin, N, divisors)) {
            count++;
            cout << Convert(jamcoin).substr(32-N);
            for (int i = 2; i <=10; ++i)
                cout << " " << divisors[i];
            cout << '\n';
        }
    }
}

bool is_prime(unsigned long num, int&divisor) {
    if (num < 2){
        divisor = -1;
        return false;
    }
    for (int i = 2; i <= sqrt(num); ++i) {
        if (num % i == 0) {
            divisor = i;
            return false;
        }
    }
    return true;
}

unsigned long convert_to_base(unsigned int number, int base, int N) {
    unsigned long total = 0;
    for (int i = 0; i < N; ++i) {
        unsigned short last_digit = number & 1;
        number = number >> 1;
        if (last_digit == 1)
            total += pow(base, i);
    }
    // cout << "Base: " << base << " val: " << total << endl;
    return total;
}

bool is_jamcoin(unsigned int number, int N, int nontrivial_divisor[]) {
    int divisor;
    for (int i = 2; i <= 10; ++i) {
        unsigned long base_i_representation = convert_to_base(number, i, N);
        bool prime = is_prime(base_i_representation, divisor);
        if (prime) {
            return false;
        }
        else {
            nontrivial_divisor[i] = divisor;
        }
    }
    return true;
}

string Convert(unsigned int val) {
    string bin = "";
   unsigned int mask = 1 << (sizeof(int) * 8 - 1);
   for(int i = 0; i < sizeof(int) * 8; i++) {
      if( (val & mask) == 0 )
         bin += '0';
      else
         bin += '1';
      mask  >>= 1;
   }
   return bin;
}
