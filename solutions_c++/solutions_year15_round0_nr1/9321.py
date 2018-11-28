#include <iostream>
#include <vector>

using namespace std;

int process(const vector<int>& S) {
    int s = S.size();
    int friends = 0;
    int standing = 0;
    for(int i = 0; i < s; ++i) {
        if(standing < i) {
            // We need friends.
            friends += i-standing;
            standing = i;
        }
        standing += S[i];
    }
    return friends;
}




int main () {
    int n;
    cin >> n; // Test cases.
    for(int i = 0; i < n; ++i) {
        int Smax;
        cin >> Smax;
        vector<int> S(Smax+1);
        for(int j = 0; j <= Smax; ++j) {
            char c;
            cin >> c;
            S[j] = c-'0';
        }
        cout << "Case #" << i+1 << ": " << process(S) << endl;
    }
}
