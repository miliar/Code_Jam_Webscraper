#include <iostream>
#include <cstdio>

using namespace std;

int parity[2501], T, N, x;

int main() {
    freopen("Rank.in", "r", stdin);
    freopen("Rank.out", "w", stdout);

    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> N;

        for(int j = 0; j < 2501; j++) {
            parity[j] = 0;
        }

        for(int j = 0; j < 2*N-1; j++) {
            for(int k = 0; k < N; k++) {
                cin >> x;
                parity[x] = (parity[x]+1)%2;
            }
        }

        cout << "Case #" << (i+1) << ":";
        for(int j = 1; j <= 2500; j++) {
            if(parity[j])
                cout << " " << j;
        }
        cout << endl;
    }
}
