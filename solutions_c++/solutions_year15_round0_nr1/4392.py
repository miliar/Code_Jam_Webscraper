#include <iostream>
#include <vector>

using namespace std;

int solve() {
    int standing = 0;
    int max = 0, i = 0;
    int res = 0, ibuffer = 0;
    char buffer;

    cin >> max;
    
    for (i = 0; i <= max; ++i) {
        cin >> buffer;
        ibuffer = buffer - '0';

        if (i <= standing) {
            standing += ibuffer;
        } else {
            res += (i - standing);
            standing += (i - standing) + ibuffer;
        }
    }

    return res;
}


int main () {

    int nb_case = 0;
    cin >> nb_case;
    
    int res = 0;

    for (int i = 0; i < nb_case; ++i) {
        res = solve();
        cout << "Case #" << (i+1) << ": " << res << '\n';         
    }
}
