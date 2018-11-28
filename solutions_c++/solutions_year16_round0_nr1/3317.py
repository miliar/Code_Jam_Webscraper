#include <cstdio>
#include <iostream>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>

#define ULL unsigned long long

using namespace std;

int T, tcase, N;
ULL num;

int threshold;
char buffer[15];
int szn;

int digit[10];

bool isNull(int i) {
    return i;
}

int main()
{
    cin >> T;
    tcase = 1;
    while (tcase<=T) {
        memset (digit, 0, sizeof(int)*10);
        cin >> N;

        num = N;
        szn = sprintf(buffer, "%d", N);
        threshold = pow(10,szn+1);

        while ( find(digit,digit+10,0)!=digit+10 ) {
            if (threshold--) {
                szn = sprintf(buffer, "%llu", num);
            } else {
                szn = sprintf(buffer, "INSOMNIA");
                break;
            }

            for (int i=0; i<szn; ++i) {
                digit[buffer[i]-'0'] = 1;
            }
            num += N;
        }

        cout << "Case #" << tcase++ << ": " << buffer << endl; 
    }
}
