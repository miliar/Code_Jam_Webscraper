#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <bitset>
#include <cmath>

using namespace std;


bool isPrime(unsigned long long value, int * div) {
    // value is not / 2
    for (int i=3;i<std::sqrt(value);i+=2)
    {
        if (value % i == 0) {
            *div = i;
            return false;
        }
    }
    return true;
}

int main()
{
    //ifstream fin("input.in");
    ifstream fin("C-small-attempt0.in");
    //ifstream fin("C-large.in");
    ofstream fout("output.out");

    if (!fin.is_open()) cout << "input.in open fail" << endl;
    if (!fout.is_open()) cout << "output.out open fail" << endl;

    int numCase;
    fin >> numCase;

    int caise;
    for (caise = 0; caise < numCase; caise++)
    {
        int n,j;
        fin >> n;
        fin >> j;

        cout << "Case #" << (caise + 1) << ":" << endl;
        fout << "Case #" << (caise + 1) << ":" << endl;

        u_int32_t coinUInt = 0x8001 - 2;
        //u_int32_t coinUInt = 0x80000001 - 2;
        for (int i = 0 ; i < j ; ) {
            coinUInt += 2;
            bitset<16> coinBiteSet = bitset<16>(coinUInt);
            int dividers[9];
            bool primeFound = false;
            for (int base = 2 ; base <= 10 ; base++) {
                unsigned long long value = 0;
                for (int bit = 0 ; bit <n ; bit++){
                    if (coinBiteSet[bit] )
                        value += std::pow(base,bit);
                }
                //cerr << "value in base " << base << " is " << value << endl;
                if (isPrime(value, &dividers[base-2])) {
                    primeFound = true;
                    break;
                }
               // cerr << value / dividers[base-2] << " " << value % dividers[base-2] << endl;
                //    cout << dividers[dIt] << endl;
                //      fout << dividers[dIt] << endl ;
            }

            if (!primeFound) {
                cout << coinBiteSet;
                fout << coinBiteSet;
                for (int b = 0 ; b < 9 ; b++) {
                    cout << " " << dividers[b] ;
                    fout << " " << dividers[b] ;
                }
                cout << endl;
                fout << endl ;
                i++;
            }
        }

    }

    fin.close();
    fout.close();
    return 0;
}
