#include <bits/stdc++.h>
using namespace std;

const int dx[5] = {-1, 1, 0, 0};
const int dy[5] = {0, 0, 1, -1};

string D = "^v><";

int main() {
    
    ifstream cin("testA.in");
    ofstream cout("testA.out");

    int t; cin >> t;
    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        int n, m; cin >> n >> m;
        vector<string> A(n);
        for(int i = 0; i < n; ++i)
            cin >> A[i];
        
        int ans = 0;
        bool possible = true;

        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j)
                if(A[i][j] != '.') {
                    bool canSwitch = false;
                    int cost = 1;
                    for(int d = 0; d < 4; ++d) {
                        pair<int, int> now = make_pair(i, j);
                        bool has = false;
                        while(now.first >= 0 && now.first < n && now.second >= 0 && now.second < m) {
                            if((now.first != i || now.second != j) && A[now.first][now.second] != '.') {
                                has = true;
                                break;
                            }
                            now.first += dx[d];
                            now.second += dy[d];
                        }
                        if(has) {
                            canSwitch = true;
                            int temp = 0;
                            if(D[d] != A[i][j])
                                temp = 1;
                            cost = min(cost, temp);
                        }
                    }

                    if(!canSwitch)
                        possible = false;
                    else
                        ans += cost;
                }

        if(!possible)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }
}
