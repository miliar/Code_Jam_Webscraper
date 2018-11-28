#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <numeric>

using namespace std;

int T, N;

int main()
{
    ios::sync_with_stdio(false);
    cout.precision(8);

    cin >> T;
    for (int t = 1; t <= T; t++) {
        int P[26] = {};
        string O;

        cin >> N;
        for (int n = 0; n < N; n++) cin >> P[n];
        
        int cc = 0;
        int C = accumulate(begin(P), end(P), 0);

        for (int cnt = 0; cnt < C; cnt++) {
            while (P[cc] == 0) cc = (cc + 1) % N;

            P[cc]--;
            O += 'A' + cc;
            cc = (cc + 1) % N;

            if (cnt % 2) O += " ";
        }

        reverse(O.begin(), O.end());
        if (O[0] == ' ') O = O.substr(1);
        cout << "Case #" << t << ": " << O << endl;
    }
}
