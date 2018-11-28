#include <iostream>
using namespace std;

int main() {
    int T;
    int A, B, K;
    cin >> T;
    for (int ca=1; ca<=T; ca++) {
        cin >> A >> B >> K;
        int wins = 0;
        for (unsigned int i=0; i<A; i++) {
            for (unsigned int j=0; j<B; j++) {
                int tmp = (i & j);
                if (tmp < K && tmp >= 0) {
                    wins++;
                }
            }
        }

        cout << "Case #" << ca << ": " << wins << endl;
    }

    return 0;
}
