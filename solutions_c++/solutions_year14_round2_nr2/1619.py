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
    int A, B, K;

    void getData() {
        cin >> A >> B >> K;
    }
    void solve() {
        int ans = 0;
        for(int j = 0; j < A; j++) {
            for(int i = 0; i < B; i++) {
                if ((i &j) < K)
                    ans++;
            }
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
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    Solver* s = new Solver();
    s->run();
    return 0;
}

