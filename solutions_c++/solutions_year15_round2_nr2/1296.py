#include <bits/stdc++.h>

using namespace std;

ifstream f("b.in");

const int NMAX = 1001;
const int INF = (1<<30);
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
int dp[17][17][17*17];

int fa(int i, int j, int n){

    //cout << i << " " << j << " " << n << "\n";
    //if (dp[i][j][n] != INF) return dp[i][j][n];
    vector< pair<int,int> > v;
    vector< int> v2;
    int ans = INF;
            v.clear();
        for(int k=1; k<=i; ++k){
            for(int l=1; l<=j; ++l){
                    v.push_back(make_pair(k, l));
                }
            }
    for(int k=0; k<(1<< ((int)v.size()) ); ++k){
                //cout << k << '\n';
        v2.clear();
        for(int l=0; l<v.size(); ++l){
            if (k & (1<<l)){
                v2.push_back(l);
            }
        }
        if (v2.size() == n){
        int ceva =0;
        for(int l=0; l<v2.size(); ++l){
            int currX = v[ v2[l] ].first;
            int currY = v[ v2[l] ].second;
            //cout << currX << "  "<< currY << "\n";
            for(int t=0; t<4; ++t){
                int newX = currX + dx[t];
                int newY = currY + dy[t];
                    for(int p=l+1; p<v2.size(); ++p){
                        int x = v[ v2[p] ].first;
                        int y = v[ v2[p] ].second;
                        if (x == newX && y == newY){
                                //dp[i][j][v2.size()]++;
                                //dp[i][j][v2.size()] = min(dp[i][j][v2.size()-1] + 1, dp[i][j][v2.size()]);
                            ++ceva;
                        }
                    }
                    //}
            }
        }
        //cout << ceva << "\n";
        ans = min(ans, ceva);
        }

    }
    if (ans == INF) return 0;
    return ans;

}


void scrie(int testNo, int ans){
    printf("Case #%d: %d\n", testNo, ans);
}


int main(){
    freopen("b.out", "w", stdout);
    //fa();
    for(int i=0; i<17; ++i){
        for(int j=0; j<17; ++j){
            for(int k=1; k<17*17; ++k) dp[i][j][k] = INF;
        }
    }
    int t; f>> t;
    for(int i=1; i<=t; ++i){
        int l, r, n;
        f >> l >> r >> n;
        scrie(i, fa(l, r, n));
    }
    return 0;
}
