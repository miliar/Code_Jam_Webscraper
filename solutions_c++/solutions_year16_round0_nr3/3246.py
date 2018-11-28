#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, N, J;
    cin >> T >> N >> J;

    string baseHalfCoinJam, halfCoinJam;

    baseHalfCoinJam.push_back('1');
    for (int i = 0; i < N/2-2;i++)
        baseHalfCoinJam.push_back('0');
    baseHalfCoinJam.push_back('1');

    int jTemp;
    unsigned long int divisor;

    cout << "Case #1:" << endl;

    for (int j = 1; j <= J; j++) {
        jTemp = j;
        int k = 1;
        halfCoinJam = baseHalfCoinJam;
        while (jTemp > 0) {
            halfCoinJam[k] = '0' + jTemp%2;
            jTemp = jTemp/2;
            k++;
        }
        cout << halfCoinJam + halfCoinJam << " ";
        for (int a = 2; a <= 10; a++) {
            divisor = 1;
            for (int h = 0; h < N/2; h++)
                divisor = divisor*a;
            divisor++;
            cout << divisor << " ";
        }
        cout << endl;
    }

    return 0;
}
