
#include <stdlib.h>
#include <iostream>
#include <string>


using namespace std;

char val[10000];
char M[10000][8];
const char one = '1',
     ci = 'i',
     cj = 'j',
     ck = 'k',
     mone = '2', // -1
     mci = 'l', // -i
     mcj = 'm', // -j
     mck = 'n'; // -k
char X[] = {one, ci, cj, ck, mone, mci, mcj, mck};
char MUL[8][8] = {{one, ci, cj, ck},
                  {ci, mone, ck, mcj},
                  {cj, mck, mone, ci},
                  {ck, cj, mci, mone}};

int getidx(char a) {
    switch(a) {
        case one:
            return 0;
        case ci:
            return 1;
        case cj:
            return 2;
        case ck:
            return 3;
        default:
            cout << a << " whoops" << endl;
            return -1;
    }
}

char mul(char a, char b) {
    bool sign = false;
    if(a == mone) {
        a = one;
        sign = true;
    }
    if(a >= mci && a <= mck) {
        a -= 3;
        sign = true;
    }
    if(b == mone) {
        b = one;
        sign = !sign;
    }
    if(b >= mci && b <= mck) {
        b -= 3;
        sign = !sign;
    }
    int i = getidx(a), j = getidx(b);
    char res = MUL[i][j];
    if(sign) {
        if(res == mone) {
            res = one;
        } else if(res == one) {
            res = mone;
        } else if(res >= mci) {
            res -= 3;
        } else if(res <= ck) {
            res += 3;
        }
    }
    return res;
}

int main()
{
    int t;
    cin >> t;

    for ( int tcase = 0; tcase < t; tcase += 1 ) {
        int x, l;
        string line;
        cin >> l >> x;
        cin.ignore();
        getline(cin, line);
        if( l * x < 3 ) {
            cout << "Case #" << (tcase + 1) << ": NO" << endl;
            continue;
        }

        for ( int i = 0; i < x; i += 1 ) {

            for ( int j = 0; j < l; j += 1 ) {
                val[i * l + j] = line[j];
                char a, b;
                
                for ( int k = 0; k < 8; k += 1 ) {
                    char prev;
                    if(i+j == 0) {
                        prev = X[k];
                    } else {
                        prev = M[i * l + (j - 1)][k];
                    }
                    M[i * l + j][k] = mul(prev, line[j]);
                }
            }
        }
#ifdef  DEBUG
        cout << "M: " << endl;
        for(int i = 0; i < (l * x); i++) {

            for ( int k = 0; k < 8; k += 1 ) {
                cout << M[i][k] << " ";
            }
            cout << endl;
        }
#endif
        

        bool foundjk = false;
        for(int b = 0; b < (l * x - 2); b++) {
            if(M[b][0] != 'i') {
                continue;
            }
            for(int e = b + 1; e < (l * x - 1); e++) {
                
                int jidx = -1;
                for ( int k = 0; k < 8; k += 1 ) {
                    if(M[b+1][k] == val[b+1]) {
                        jidx = k;
                        break;
                    }
                }
                if(jidx < 0) {
                    cout << "really?" << endl;
                    continue;
                }
                if(M[e][jidx] != 'j') {
                    continue;
                }

                int kidx = -1;
                for(int k = 0; k < 8; k++) {
                    if(M[e+1][k] == val[e+1]) {
                        kidx = k;
                        break;
                    }
                }
                if(kidx < 0) {
                    cout << "really?" << endl;
                    continue;
                }

                if(M[l * x - 1][kidx] == 'k') {
                    foundjk = true;
                    break;
                }
            }
            if(foundjk) break;
        }
        cout << "Case #" << (tcase + 1) << ": ";
        cout << (foundjk ? "YES" : "NO") << endl;
    }
    return 0;
}
