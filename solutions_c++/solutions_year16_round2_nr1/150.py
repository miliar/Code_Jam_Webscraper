#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream cin("testA.in");
    ofstream cout("testA.out");
    
    int t; cin >> t;
    
    map<int, string> M;
    M[0] = "ZERO"; //
    M[1] = "ONE";
    M[2] = "TWO"; //
    M[3] = "THREE";
    M[4] = "FOUR"; //
    M[5] = "FIVE";
    M[6] = "SIX"; //
    M[7] = "SEVEN";
    M[8] = "EIGHT"; //
    M[9] = "NINE";

    for(int t_case = 0; t_case < t; ++t_case) {
        cout << "Case #" << t_case + 1 << ": ";
        string S; cin >> S;

        vector<int> f(26, 0);
        for(auto c : S)
            f[c - 'A']++;
        
        vector<int> taken(10, 0);
        vector<int> sol;
        
        for(int it = 0; it < 10; ++it) {
            for(int i = 0; i < 26; ++i) {
                int cnt = 0, idx = -1;
                char c = char(i + 'A');
                string elem = "a";
                elem[0] = c;


                for(int j = 0; j < 10; ++j)
                    if(!taken[j]) {
                        if(M[j].find(elem) != string::npos) {
                            idx = j;
                            cnt++;
                        }
                    }

                if(cnt == 1) {
                    taken[idx] = 1;
                    while(f[i]) {
                        sol.push_back(idx);
                        for(auto l : M[idx])
                            f[l - 'A']--;
                    }
                }
            }
        }
        
        string ans;

        sort(sol.begin(), sol.end());
        for(auto temp : sol)
            ans += to_string(temp);

        cout << ans << "\n";
    }
}
