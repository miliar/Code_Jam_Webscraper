#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T;
    string S;
    int moves;

    cin >> T;

    for(int i = 1; i <= T; ++i) {
        cin >> S;
        moves = 0;
        if (S[0] == '-') {
            --moves;
        }

        for (int j = 0; j < S.length(); ++j) {
            if (S[j] == '-') {
                while (S[j] == '-') {
                    ++j;

                    if (j >= S.length()) {
                        break;
                    }
                }

                moves += 2;
            }
        }

        cout << "Case #" << i << ": " << moves << endl;
    }

	return 0;
}
