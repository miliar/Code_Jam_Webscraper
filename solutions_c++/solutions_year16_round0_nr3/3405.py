#include <cmath>
#include <bitset>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.ignore();
    int N, J;
    cin >> N >> J;
    vector<vector<long long>> jamcoins(J, vector<long long>(10));
    int coin = 1;
    coin <<= N - 1;
    coin += 1;
    int cur = 0;
    while (cur < J) {
        jamcoins[cur][0] = coin;
        for (int i = 2; i <= 10; i++) {
            int temp = coin;
            long long decimal = 0;
            long long power = 1;
            for (int j = 0; j < N; j++) {
                if (temp & 1) {
                    decimal += power;
                }
                temp >>= 1;
                power *= i;
            }
            //cout << "base " << i << ": " << decimal << endl;
            int r = sqrt(decimal);
            int d = 3;
            while ((decimal % d) && d < r) {
                d += 2;
            }
            if(decimal % d == 0) {
                jamcoins[cur][i - 1] = d;
                if(i == 10){
                    cur++;
                }
            }
            else break;
        }
        coin += 2;

    }
    cout << "Case #1:\n";
    for(int i = 0; i < J; i++) {
        string coin = bitset<32>(jamcoins[i][0]).to_string();
        coin.erase(0, 32 - N);
        cout << coin;
        for(int j = 1; j < 10; j++) {
            cout  << " " << jamcoins[i][j];
        }
        cout << endl;
    }
}
