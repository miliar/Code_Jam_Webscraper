#include <iostream>
#include <stdlib.h>
#include <cstring>

#define DEBUG

using namespace std;

int A[1000];
int C[1000];

void compute(int n) {

    C[0] = A[0];
    int prev = A[0];
    for ( int i = 1; i < n; i += 1 ) {
        C[i] = A[i] + prev;
        prev = C[i];
    }
}

int main()
{
    int t;
    cin >> t;

    for ( int i = 0; i < t; i += 1 ) {
        memset(A, 0, sizeof(A));
        memset(C, 0, sizeof(C));
        int s;
        char c;
        cin >> s;
        s++;
        
        for ( int j = 0; j < s; j += 1 ) {
            cin >> c;
            A[j] = (c - '0');
        }
        compute(s);

        int add = 0;
        for ( int j = 1; j < s; j += 1 ) {
            int total = C[j - 1] + add;
            if(total < j) {

                add += (j - total);
                A[0] += (j - C[j - 1]);
            }
        }
        cout << "Case #" << (i + 1) << ": " << add << endl;
    }
    return 0;
}
