#include <iostream>
#include <set>
using namespace std;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        set<int> s;
        int N;
        cin >> N;
        int temp;
        for(int n = 0; n < (N * 2 - 1) * N; n++) {
             cin >> temp;
             if(!s.insert(temp).second) s.erase(temp);
        }
        cout << "Case #" << t << ":";
        for(int i : s) {
            cout << ' ' << i;
        }
        cout << '\n';
    }
    return 0;
}
