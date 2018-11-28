#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <thread>

using namespace std;

#define ll long long

int N, S;

double P[1000][3], V[1000][3];
double D[1000][1000];

bool solve(double jump) {
    bool vis[1000] = {0};
    deque<pair<int,int>> Q;
    Q.emplace_back(0, 0);
    vis[0] = true;

    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop_front();
        int x = cur.first;
        if (x == 1) {
            return true;
        }
        for (int i=0;i<N;++i) {
            if (!vis[i] && D[x][i] <= jump) {
                Q.emplace_back(i, cur.second + 1);
                vis[i] = true;
            }
        }
    }

    return false;
}

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        
        cin>>N>>S;
        for (int i=0;i<N;++i) {
            cin>>P[i][0];
            cin>>P[i][1];
            cin>>P[i][2];
            cin>>V[i][0];
            cin>>V[i][1];
            cin>>V[i][2];
        }
        for (int i=0;i<N;++i) {
            for (int j=i+1;j<N;++j) {
                double s = 0;
                for (int k=0;k<3;++k) {
                    double d = P[i][k] - P[j][k];
                    s += d*d;
                }
                D[i][j] = sqrt(s);
                D[j][i] = D[i][j];
            }
        }


        double high = 1000*1000*1000, low = 0;
        while (high - low > 1e-9) {
            double mid = (high+low)/2;
            if (solve(mid)) {
                high = mid;
            } else {
                low = mid;
            }
        }

        printf("Case #%d: %.9f\n", t, high);
    }
}
