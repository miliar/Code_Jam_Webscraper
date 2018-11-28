#include <iostream>
using namespace std;

#define max_l 1001
int flip_end[max_l];

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        string S;
        int K;
        cin >> S >> K;

        int l = S.length(), limit = l-K, flip_count = 0, p = 0;
        bool is_flipped_mode = false;
        bool is_impossible = false;

        for (int i=0; i <= l; ++i) {
            flip_end[i] = 0;
        }

        for (int i=0; i <= limit; ++i) {
            p -= flip_end[i];
            if (is_flipped_mode && !p) {
                is_flipped_mode = false;
            }

            if ((!is_flipped_mode && S[i] == '-') ||
                    (is_flipped_mode &&
                            (((p&1) && S[i] == '+') || (!(p&1) && S[i] == '-')))) {
                ++flip_count;
                is_flipped_mode = true;
                ++p;
                flip_end[i + K] = 1;
            }
        }

        for (int i = limit + 1; i < l; ++i) {
            p -= flip_end[i];
            if (is_flipped_mode && !p) {
                is_flipped_mode = false;
            }

            if ((!is_flipped_mode && S[i] == '-') ||
                (is_flipped_mode &&
                 (((p&1) && S[i] == '+') || (!(p&1) && S[i] == '-')))) {
                is_impossible = true;
            }
        }

        if (is_impossible) {
            cout << "Case #" << test << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << test << ": " << flip_count << endl;
        }
    }

    return 0;
}