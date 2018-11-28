#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<int> solve(const map<int, int>& m) {
    vector<int> ret;
    for(const auto& item: m) {
        if (item.second % 2) {
            ret.push_back(item.first);
        }
    }

    return ret;
}

int main() {
    int T, N;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        cin >> N;
        map<int, int> M;
        for (int j = 0; j < 2*N - 1; j++) {
            for (int i = 0; i < N; i++) {
                int r;
                cin >> r;
                M[r] += 1;
            }
        }
        auto S = solve(M);
        cout << "Case #" << c << ":";
        for (auto item : S)
            cout << " " << item;
        cout << endl;
    }

    return 0;
}
