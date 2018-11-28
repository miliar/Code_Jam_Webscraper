#include <iostream>
#include <string>
#include <cmath>
#include <bitset>

#define BITS 16

using namespace std;

unsigned long getDivisor(unsigned long long n) {
    if (n < 2) return 0;
    if ((n % 2) == 0) return 2; 
    unsigned long sqrtN = (unsigned long)sqrt((double)n);
    for (unsigned long i = 3; i < sqrtN; i+=2)
        if ((n % i) == 0) return i;
    return 0;
}

void jamcoin(unsigned short c, unsigned short n, unsigned short j) {
    cout << "Case #" << c << ": " << endl;
    if (n == 2) return; 

    unsigned short cnt = 0;
    unsigned long divs[8];

    while (j > 0) {
        //cout << j << " jam coins remaining" << endl;
        bitset<BITS-2> bs(cnt++);          // bitset<n-2> requires constant int
        string perm = "1" + bs.to_string() + "1";
        int i;
        for (i = 2; i <= 10; ++i) {
            unsigned long div; 
            if ((div = getDivisor(stoull(perm, nullptr, i))) == 0) break;
            else divs[i-2] = div;
        }
        if (i > 10) {
            cout << perm << " "; 
            for (unsigned short d = 0; d < 9; ++d)
                cout << divs[d] << " ";
            cout << endl;
            j--;
        }
    }
}


int main(int argc, char * argv[]) {
    unsigned short t;
    cin >> t;

    for (unsigned short i = 1; i <= t; ++i) {
        unsigned short n, j;
        cin >> n;
        cin >> j;
        jamcoin(i, n, j);
    }

    return 0;
}
