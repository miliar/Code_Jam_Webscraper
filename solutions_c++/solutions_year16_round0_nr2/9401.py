#include<bits/stdtr1c++.h>
using namespace std;

int T; string S;
vector<char> V;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        cin >> S;
        V = vector<char>();
        for (int i = 0; i < (int)S.size(); ++i)
            if (V.size() == 0 || V.back() != S[i])
                V.push_back(S[i]);
        if (V.back() == '+')
            V.pop_back();
        cout << V.size() << "\n";
    }
    
    return 0;
}
