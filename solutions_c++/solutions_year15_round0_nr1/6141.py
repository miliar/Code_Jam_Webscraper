#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
    ifstream fi("as.in");
    ofstream fo("aso.txt");

    int T;
    fi >> T;
    for (int k = 1; k <= T; k++) {
        int Smax;
        fi >> Smax;
        int ans = 0, total = 0;
        for (int i = 0; i <= Smax; i++) {
            char aux;
            fi >> aux;
            int curent = aux - '0';
            if (total < i && curent > 0) {
                ans += i - total;
                total = i;
            }
            total += curent;
        }
        fo << "Case #" << k << ": " << ans << endl;
    }
    return 0;
}
