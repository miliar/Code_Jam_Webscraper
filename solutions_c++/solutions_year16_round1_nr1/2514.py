#include <iostream>
#include <string>
#include <sstream>
#include <vector>


using namespace std;

int main() {
    int T;
    cin >>T;
    for (int t = 0 ;t < T; ++t) {
        string S;
        cin >> S;

        stringstream res;
        vector<int> pos;
        vector<bool> f(S.size(), true);
        pos.push_back(0);
        f[0] = false;
        int max_pos = 0;
        for (int i = 1; i < S.size(); ++i) {
            if (S[i] >=  S[max_pos]) {
                pos.push_back(i);
                max_pos = i;
                f[i] = false;
            }
        }
        
        for (int i = 0; i < pos.size(); ++i) {
            res << S[pos[pos.size()-i-1]];
        }
        for (int i = 0; i < S.size(); ++i) {
            if (f[i]) {
                res << S[i];
            }
        }
        cout << "Case #" << t+1 << ": " << res.str() << endl;
    }
    return 0;
}
