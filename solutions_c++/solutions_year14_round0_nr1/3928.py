#include <iostream>
#include <bitset>
#include <string>
#include <cmath>
#include <cstdio>

using namespace std;

void solve_case(int case_num) {
    bitset<16> rows[2];

    for (int i = 0; i < 2; ++i) {
        int answer;
        cin >> answer;

        for (int j = 0; j < 4; ++j) {
            unsigned int bits = 0;

            for (int k = 0; k < 4; ++k) {
                int card;
                cin >> card;
                bits |= 1 << (card - 1);
            }

            if (j == answer - 1) {
                rows[i] = bitset<16>(bits);
            }
        }
    }

    bitset<16> result = rows[0] & rows[1];
    string message;
    if (result.count() == 0) {
        cout << "Case #" << case_num << ": Volunteer cheated!" << endl;
    } else if (result.count() > 1) {
        cout << "Case #" << case_num << ": Bad magician!" << endl;
    } else {
        int card = log2(result.to_ulong()) + 1;
        cout << "Case #" << case_num << ": " << card << endl;
    }

}


int main(int argc, char** argv) {
    int num_cases;
    cin >> num_cases;
    for (int i = 0; i < num_cases; ++i) {
        solve_case(i + 1);
    }

    return 0;
}

