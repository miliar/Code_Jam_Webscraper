#include "iostream"

using namespace std;

int main() {
        int T;
        cin >> T;
        for (int t = 1; t <= T; ++t) {
                int num_friends = 0;
                int num_standing = 0;
                int S_max;
                cin >> S_max;
                for (int i = 0; i <= S_max; ++i) {
                        char c;
                        cin >> c;
                        int S_i = c - '0';
                        int diff = i - num_standing;
                        if (diff > 0) {
                                num_friends += diff;
                                num_standing += diff;        
                        }
                        num_standing += S_i;
                }
                cout << "Case #" << t << ": " << num_friends << endl;
        }
        return 0;
}
