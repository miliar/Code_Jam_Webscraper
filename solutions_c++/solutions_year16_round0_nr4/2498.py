#include <iostream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;


void calc(int K, int C, int S) {
    long long p = pow(K, C-1);
    for (int i = 0; i < S; i++) {
        cout << " " << (i * p)+1;
    }
}

int main() {
	int testCases;
    cin >> testCases;
    int K, C, S;

    for (int i = 1; i <= testCases; i++) {
        cin >> K >> C >> S;
        cout << "Case #" << i << ":";
        calc(K, C, S);
        cout << endl;
    }

    return 0;
}
