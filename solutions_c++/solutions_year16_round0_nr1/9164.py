#include <iostream>
#include <string>
#include <climits>

using std::endl;
using std::cin;
using std::cout;
using std::string;

unsigned long doIt(unsigned long n) {
    unsigned int seen = 0;

    unsigned long m = n;

 //   cout << "N == " << n << ": "; 
    for (;;) {
        unsigned long x = m;
        while (x != 0) {
            int l = x % 10;
            seen = seen | 1 << l;
            x = x / 10;
        }

        if (seen != 0x3ff) {
            if (m > ULONG_MAX - n) {
                cout << "OVERFLOW: N == " << n << " last == " << m << endl;
                break;
            }

            m += n;
        } else {
            return m;
//            cout << m << endl;
            break;
        }
    }
}

void doCase(int caseNum) {
    unsigned long N;
    cin >> N;

    if (N == 0) {
        cout << "Case #" << caseNum << ": INSOMNIA" << endl;
    } else {
        cout << "Case #" << caseNum << ": " << doIt(N) << endl;
    }
}

int main() {
    int numCases;
    cin >> numCases;

    for (int i = 0; i < numCases; i++) {
        doCase(i+1);
    }
}
