#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
    long T, N;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        set<long> ans;
        for (int i = 0; i < N * (2*N - 1); i++) {
            long tmp;
            cin >> tmp;
            if (ans.count(tmp)) ans.erase(tmp);
            else (ans.insert(tmp));
        }
        cout << "Case #" << t << ":";
        for (auto x : ans) cout << " " << x;
        cout << endl;
    }
}
