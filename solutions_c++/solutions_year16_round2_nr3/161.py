#include <bits/stdc++.h>
using namespace std;

bool match(int node, vector<vector<int>> &G, vector<int> &used, vector<int> &L, vector<int> &R) {
    if(used[node])
        return false;
    used[node] = 1;

    for(auto temp : G[node]) {
        if(R[temp] == -1) {
            L[node] = temp;
            R[temp] = node;
            return true;
        }
    }

    for(auto temp : G[node])
        if(match(R[temp], G, used, L, R)) {
            L[node] = temp;
            R[temp] = node;
            return true;
        }

    return false;
}

int getMatching(vector<vector<int>> &G, int m) {
    int n = G.size();
    bool ok = true;
    
    vector<int> used;
    vector<int> L(n, -1);
    vector<int> R(m, -1);

    int ans = 0;
    
    while(ok) {
        ok = false;
        used = vector<int> (n, 0);
        for(int i = 0; i < n; ++i)
            if(L[i] == -1 && match(i, G, used, L, R)) {
                ans++;
                ok = true;
            }
    }
    
    return ans;
}

int main() {
    ifstream cin("testC.in");
    ofstream cout("testC.out");
    
    int t; cin >> t;
    
    for(int t_case = 0; t_case < t; ++t_case) {
        cout << "Case #" << t_case + 1 << ": ";
        int w; cin >> w;
        
        vector<pair<string, string>> A(w);
        
        map<string, int> f;
        map<string, int> s;
        
        int n = 0, m = 0;

        for(int i = 0; i < w; ++i) {
            cin >> A[i].first >> A[i].second;
            if(f.find(A[i].first) == f.end())
                f[A[i].first] = n++;
            if(s.find(A[i].second) == s.end())
                s[A[i].second] = m++;
        }
        
        vector<vector<int>> G(n, vector<int> ());

        for(int i = 0; i < w; ++i)
            G[f[A[i].first]].push_back(s[A[i].second]);

        int ans = getMatching(G, m);
        
        if(t_case == 3)
            cerr << n << " " << m << " " << ans << "\n";

        cout << w - (n + m - ans) << "\n";
    }
}
