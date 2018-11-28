#include <bits/stdc++.h>
using namespace std;

map<vector<string>, bool> memo;

bool good(vector<string> A) {
    
    if(memo.find(A) != memo.end())
        return memo[A];


    int n = A.size();
    if(n == 1) {
        if(A[0][0] == '0')
            return memo[A] = false;
        return memo[A] = true;
    }
    
    vector<int> pos(n, 0);
    for(int i = 0; i < n; ++i)
        pos[i] = i;
    
    bool has = false;

    do {
        bool ok = true;
        for(int i = 0; i < n; ++i)
            if(A[i][pos[i]] != '1')
                ok = false;
        if(ok) {
            has = true;
            break;
        }
    } while(next_permutation(pos.begin(), pos.end()));
    
    if(!has)
        return memo[A] = false;

    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j) {
            if(A[i][j] == '0')
                continue;
            vector<string> B;
            for(int x = 0; x < n; ++x) {
                if(x == i)
                    continue;
                string temp = "";
                for(int y = 0; y < n; ++y) {
                    if(y == j)
                        continue;
                    temp += A[x][y];
                }
                B.push_back(temp);
            }

            if(!good(B)) {
                memo[A] = false;
                return false;
            }
        }

    memo[A] = true;
    return true;
}

int main() {
    ifstream cin("testD.in");
    ofstream cout("testD.out");

    int t; cin >> t;
    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        cerr << t_case << "\n";

        int n; cin >> n;
        vector<string> A(n);
        vector<pair<int, int>> f;

        for(int i = 0; i < n; ++i) {
            cin >> A[i];
            for(int j = 0; j < n; ++j)
                if(A[i][j] == '0')
                    f.push_back({i, j});
        }

        int sz = f.size();
        int ans = 1e9;
        
        for(int mask = 0; mask < (1 << sz); ++mask) {
            vector<string> tmp = A;
            int cost = 0;

            for(int i = 0; i < sz; ++i)
                if((1 << i) & mask) {
                    cost++;
                    tmp[f[i].first][f[i].second] = '1';
                }

            if(good(tmp))
                ans = min(ans, cost);
        }

        cout << ans << "\n";
    }
}
