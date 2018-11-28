#include <cstring>
#include <cstdio>

#include <iostream>
#include <string>

using namespace std;

const string NUMBERS[] = { "ZERO", "ONE", "TWO",
                           "THREE", "FOUR", "FIVE",
                           "SIX", "SEVEN", "EIGHT",
                           "NINE" };
const char KEY[] = {'Z','O','W','T','U','F','X','S','G','I'};

/*
Z=0
W=2
U=4
X=6
G=8

O=1
T=3
F=5
S=7
I=9
*/

int freq[26];

int ctoi(char c) { return (int)(c-'A'); }

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T = 0;
    string S;

    cin >> T;

    int result[10] = {0};
    char ch = 0;
    memset(freq, 0, sizeof(freq));
    for ( int i = 0; i < T; ++i ) {
        cout << "Case #" << i+1 << ": ";

        cin >> S;
        int sLen = S.length();
        for ( int j = 0; j < sLen; ++j ) {
            ++freq[ctoi(S[j])];
        }
 
        for ( int j = 0; j <= 9; j+=2 ) {
            result[j] = freq[ctoi(KEY[j])];
            for ( int k = 0; k < NUMBERS[j].length(); ++k ) {
                freq[ctoi(NUMBERS[j][k])] -= result[j];
            }
        }
        for ( int j = 1; j <= 9; j+=2 ) {
            result[j] = freq[ctoi(KEY[j])];
            for ( int k = 0; k < NUMBERS[j].length(); ++k ) {
                freq[ctoi(NUMBERS[j][k])] -= result[j];
            }
        }

        for ( int j = 0; j < 10; ++j ) {
            for ( int k = 0; k < result[j]; ++k ) {
                putchar(j+'0');
            }
        }
        putchar('\n');
    }

    return 0;

}
