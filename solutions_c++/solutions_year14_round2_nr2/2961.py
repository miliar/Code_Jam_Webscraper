#include <iostream>

using namespace std;

int main() {
    int numCases;
    cin >> numCases;
    for (int i = 0; i < numCases; i++) {
        int A, B, K;
        cin >> A >> B >> K;
        int counter = 0;
        for (int j = 0; j < A; j++)
            for (int k = 0; k < B; k++)
                if ((j&k) < K)
                    counter++;
        cout << "Case #" << (i+1) << ": " << counter << endl;
    }
    return 0;
}