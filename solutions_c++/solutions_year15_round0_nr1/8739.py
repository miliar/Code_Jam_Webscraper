#include <iostream>
#include <vector>

using namespace std;

void test_case() {
    int Smax;
    cin >> Smax;

    int friend_count = 0;
    int up_count = 0;

    for(int Si = 0; Si <= Smax; Si++) {
        char raw;
        cin >> raw;
        int Si_count = raw - '0';

        if (up_count >= Si && Si_count > 0) {
            up_count += Si_count;
        } else if(Si_count == 0 && up_count <= Si) {
            friend_count += 1;
            up_count += 1;
        }
    }

    cout << friend_count << endl;
}

int main() {
    int T;
    cin >> T;

    for(int t = 0; t < T; t++) {
        cout << "Case #" << (t + 1) << ": ";
        test_case();
    }

    return 0;
}