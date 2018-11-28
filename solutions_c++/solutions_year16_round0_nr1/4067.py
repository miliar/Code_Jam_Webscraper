#include <iostream>
#include <vector>

using namespace std;

int digits[10];

bool checkDigits() {
   bool shouldPrint = true;
   for (int i = 0; i < 10; i++) {
       if (digits[i] <= 0) {
           shouldPrint = false;
       }
   }
   return shouldPrint;
}

void printDigits() {
    for (int i = 0; i < 10; i++) {
        cout << digits[i] << " ";
    }
    cout << endl;
}

void getValueForAll(int c, long long num, int iteration) {
    if (num == 0) {
        cout << "Case #" << c << ": INSOMNIA" << endl;
        return;
    }
    long long n = num * iteration;
    do {
        int digit = n % 10;
        digits[digit] = 1;
        n/= 10;
    } while (n > 0);

    if (checkDigits()) {
        cout << "Case #" << c << ": " << num * iteration << endl;
    } else {
        getValueForAll(c, num, iteration + 1);
    }
    
}

void clearDigits() {
   for (int i = 0; i < 10; i++) {
       digits[i] = 0;
   }
}

int main () {
   int numCases = 0;
   cin >> numCases;
   for (int i = 0; i < numCases; i++) {
       long long j;
       
       cin >> j;
       clearDigits();
       getValueForAll(i + 1, j, 1);
   }

}
