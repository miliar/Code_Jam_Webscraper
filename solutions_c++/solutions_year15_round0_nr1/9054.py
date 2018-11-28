#include <iostream>
#include <string>

using namespace std;

int solve(int Smax, string& S) {
    int stand = 0, retval = 0;
    for(int i=0; i<=Smax; ++i) {
        if(i <= stand) {
            stand += S[i] - '0';
        } else {
            int invited = i - stand;
            stand += invited + S[i] - '0';
            retval += invited;
        }
    }
    return retval;
}

int main() {
    int T;
    cin >> T;
    for(int t=1; t<=T; ++t) {
        int Smax; string S;
        cin >> Smax >> S;
        cout << "Case #" << t << ": " << solve(Smax, S) << endl;
    }
    return 0;
}
