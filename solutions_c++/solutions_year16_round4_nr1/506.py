#include<bits/stdc++.h>
#define rep(i,k,n) for(int i= (int) k;i< (int) n;i++)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;
const int limit = 1048576;
using namespace std;

// checklist
// long longi
// treść źle przeczytana
// przypadki brzegowe(min max wejście)

bool comp(vector<int> conf1, vector<int> conf2) {
    rep(i, 0, 3) {
        if(conf1[i] < conf2[i])
            return true;
        if(conf2[i] < conf1[i])
            return false;
    }
    return true;
}

void solve(vector<int> conf) {
//     cout << conf[0] << " " << conf[1] << " " << conf[2] << std::endl;
//     int a; cin >> a;
    if(conf[0] + conf[1] + conf[2] == 2) {
        if(conf[0])
            cout << "P";
        if(conf[1])
            cout << "R";
        if(conf[2])
            cout << "S";
        return;
    }
    vector<int> conf1(3), conf2(3);
    bool done = false;
    rep(i, 0, 3) {
        if(conf[i] % 2 == 0) {
            conf1[i] = conf[i] / 2;
            conf2[i] = conf[i] / 2;
        } else {
            if(done) {
                conf1[i] = conf[i] / 2;
                conf2[i] = (conf[i] + 1) / 2;
            } else {
                conf1[i] = (conf[i] + 1) / 2;
                conf2[i] = conf[i] / 2;
                done = true;
            }
        }
    }
    if(comp(conf1, conf2)) {
        swap(conf1, conf2);
    }
    solve(conf1); solve(conf2);
}

int main()
{
    ios_base::sync_with_stdio(0);
//     cin.tie(0);
    int T; cin >> T;
    rep(t, 1, T + 1) {
        int n, r, p, s; cin >> n >> r >> p >> s;
        vector<int> probe = {abs(r - p), abs(r - s), abs(p - s)};
//         cout << "WUT" << std::endl;
        if(*max_element(all(probe)) > 1)
            cout << "Case #" << t << ": IMPOSSIBLE\n";
        else {
            cout << "Case #" << t << ": ";
            solve({p, r, s});
            cout << "\n";
        }
    }
    return 0;
}