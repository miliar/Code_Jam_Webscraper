#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int coinJam [16];
long long answer[50];
long long divAnswer[50][9];

bool isPrime(long long num, int& div) {
    for (long long i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            div = i;
            return false;
        }
    }
    
    return true;
}

int main() {
    freopen("CoinJam.in", "rt", stdin);
    freopen("CoinJam.out", "wt", stdout);
    
    int numTests;
    cin >> numTests;
    
    for (int i = 0; i < numTests; ++i) {
        int N, J;
        
        cin >> N >> J;
        memset(coinJam, 0, sizeof(coinJam));
        memset(answer, 0, sizeof(answer));
        coinJam[0] = 1;
        coinJam[15] = 1;
        int cnt = 0;
        
        long long numCoinJam;
        int ind = 0;

        while (cnt < 50) {
            int newInd = ind;
            int pos = 14;
            while (newInd > 0) {
                if (newInd % 2 == 0) {
                    coinJam [pos] = 0;
                } else {
                    coinJam[pos] = 1;
                }
                --pos;
                newInd /=  2;
            }
            
            int isCoinJam = true;
            long long divs[9];
            for (int j = 2; j <= 10; ++j) {
                long long num = 0;
                for (int k = 0; k < 16; ++k) {
                    num += coinJam[k] * pow(j, k);
                }

                int div;
                if (isPrime(num, div)) {
                    isCoinJam = false;
                    break;
                }
                
                divs[j - 2] = div;
                if (j == 10) {
                    numCoinJam = num;
                }
            }
            
            if (isCoinJam) {
                answer[cnt] = numCoinJam;
                for (int p = 0; p < 9; ++p) {
                    divAnswer[cnt][p] = divs[p];
                }
                ++cnt;
            }
            ++ind;
        }
        
        cout << "Case #1:" << endl;
        
        for (int i = 0; i < 50; ++i) {
            cout << answer[i] << " ";
            for (int j = 0; j < 9; ++j) {
                cout << divAnswer[i][j] << " ";
            }
            cout << endl;
        }
    }
    
    return 0;
}
