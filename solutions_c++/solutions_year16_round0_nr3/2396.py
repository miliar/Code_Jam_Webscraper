#include <iostream> 
#include <fstream>
#include <string> 
#include <stdlib.h> 
#include <cstring>
#include <time.h> 
#include <cmath>
#include <unordered_set>
using namespace std;

long long isPrime(long long num) {
    for (long long i = 3; i <= sqrt(num); i ++) {
        if (num % i == 0) {
            return i;
        }
    }
    cout << "num: " << num << endl;

    return -1;
}

long long convert(char value[], int length, int base) {
    long long num = 0;
    for (int i = 0; i < length; i++) {
        if (value[i] == '1') {
            num += pow(base, length - i - 1);
        }
    }
    return num;
}

int main (int argc, char** args) { 
  ifstream in;
  in.open(args[1]);
  if (!in) { 
   cerr << "Can't open filebase.in" << endl; exit(2); 
  } 
  // read all input from in, write to cout 
  // in >> ... 
  // cout << ...
  srand (time(NULL));
  ofstream out("output");
  int total;
  in >> total;
  for (long long i = 0; i < total; i++) {
    out << "Case #" << i + 1 << ": \n";
    int n, j;
    in >> n >> j;
    int count = 0;
    int insuccess = 0;
    unordered_set<long long> found;
    cout << "n = " << n << endl;
    cout << "j = " << j << endl;
    while (count < j) {
        char num[n];
        num[0] = '1';
        num[n-1] = '1';
        for (int digit = 1; digit < n-1; digit ++) {
            if (rand() % 2 == 0) {
                num[digit] = '0';
            } else {
                num[digit] = '1';
            }
        }

        long long verify = convert(num, n, 10);
        if (found.find(verify) != found.end()) {
            continue;
        } else {
            found.insert(verify);
        }
        int record[9];
        bool isCorrect = true;

        for (int k = 0; k < n; k++) {
                cout << num[k];
            }

        for (int b = 2; b <= 10; b++) {
            long long converted = convert(num, n, b);
            long long res = isPrime(converted);
            if (res > 0) {
                record[b-2] = res;
            } else {
                isCorrect = false;
                insuccess ++;
                break;
            }
        }
        if (isCorrect) {
            for (int k = 0; k < n; k++) {
                out << num[k];
            }
            out <<  " ";
            for (int r = 0; r < 9; r++) {
                out << record[r] << " ";
            }
            out << endl;
            count ++;
            cout << count << "/" << j << endl;
        }
        if (insuccess % 1 == 0) {
            cout << "Failed: " << insuccess << endl;
        }
    }

    //out << count << endl;
    cout << "Finished " << i + 1 << " out of " << total << endl;
    
  }
  out.close();
  return 0; 
} 