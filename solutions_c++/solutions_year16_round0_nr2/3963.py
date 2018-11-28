#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int C=1; C<=cases; C++) {
        string P;
        cin >> P;

        char prev = P[0];
        int reduced = 1;
        for (int i=0; i<P.length(); i++) {
            if (P[i] != prev) {
                reduced++;
                prev = P[i];
            }
        }
        if (P[P.length()-1] == '+') {
            cout << "Case #" << C << ": " << reduced - 1 << endl;
        } else {
            cout << "Case #" << C << ": " << reduced << endl;
        }
    }
}
