#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
const int N = 1010;
const ll INF = 1e9;
class Solver {
public:
    int T, curTest;
    string s[110];
    int n;

    void getData() {
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >> s[i];
        }
    }
    void solve() {
        vector < pair <char, int> > v[110];
        for(int i = 0; i < n; i++) {
            int sz = (int)s[i].size();
            v[i].pb(mp(s[i][0], 1));
            for(int j = 1; j < sz; j++) {
                if (s[i][j] == s[i][j - 1]) {
                    v[i][(int)v[i].size() - 1].second++;
                } else {
                    v[i].push_back(mp(s[i][j], 1));
                }
            }
        }
        bool ok = true;
        for(int i = 1; i < n; i++) {
            ok &= (v[i - 1].size() == v[i].size());
        }

        for(int i = 1; ok && i < n; i++) {
            bool ok2 = true;
            for(int j = 0; ok2 && j < (int)v[i].size(); j++) {
                ok2 &= v[i][j].first == v[i - 1][j].first;
            }
            ok &= ok2;
        }
        if (!ok) {
            cout << "Case #" << curTest << ": Fegla Won\n";
            return;
        }
        int sum[110];
        for(int i = 0; i < 110; i++) {
            sum[i] = 0;
        }
        int ans = 0;
        for(int j = 0; j < (int)v[0].size(); j++) {
            for(int i = 0; ok && i < n; i++) {
                sum[j] += v[i][j].second;
            }
            int k = sum[j] / n;
            int r1 = 0, r2 = 0;
            for(int i = 0; ok && i < n; i++) {
                r1 += abs(k - v[i][j].second);
                r2 += abs(k + 1 - v[i][j].second);
            }
            ans += min(r1, r2);
        }
        cout << "Case #" << curTest << ": "<<ans<<"\n";

    }
    void run() {
        cin >> T;
        for(int i = 0; i < T; i++) {
            curTest = i + 1;
            getData();
            solve();
        }
    }
};
int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    Solver* s = new Solver();
    s->run();
    return 0;
}

