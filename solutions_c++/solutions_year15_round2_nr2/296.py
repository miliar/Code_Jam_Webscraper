#include <bits/stdc++.h>
using namespace std;
int dx[5] = {0, 0, 1, -1};
int dy[5] = {1, -1, 0, 0};

int main() {
    ifstream cin("testB.in");
    ofstream cout("testB.out");

    int t; cin >> t;
    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        int r, c, n; cin >> r >> c >> n;
        vector<vector<int>> A(r, vector<int> (c, 0));
        int ans = 1e6;

        for(int mask = 0; mask < (1 << (r * c)); ++mask) {
            int bits = 0;
            A = vector<vector<int>> (r, vector<int> (c, 0));

            for(int i = 0; i < (r * c); ++i)
                if((mask & (1 << i))) {
                    A[i / c][i % c] = 1;
                    bits++;
            }

            if(bits != n)
                continue;
            
            int temp = 0;

            for(int i = 0; i < r; ++i)
                for(int j = 0; j < c; ++j) 
                    for(int d = 0; d < 4; ++d) {
                        int newX = i + dx[d];
                        int newY = j + dy[d];
                        if(newX < 0 || newX >= r || newY < 0 || newY >= c)
                            continue;
                        if(A[newX][newY] && A[i][j])
                            temp++;
                    }
            ans = min(ans, temp);
        }

        cout << ans / 2 << "\n";
    }
}
