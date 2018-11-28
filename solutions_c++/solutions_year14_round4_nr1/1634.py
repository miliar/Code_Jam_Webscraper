#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void readTest(vector<int>& files, int& disc) {
    int N;
    files.clear();
    cin >> N >> disc;
    for (int i = 0; i < N; ++i) {
        int x;
        cin >> x;
        files.push_back(x);
    }
}

int solve(vector<int>& f, int X) {
    sort(f.begin(), f.end());
    //cerr << "X: " << X;
    int l = 0, r = f.size() - 1;

    int c = 0;
    while (l < r) {
        //cerr << "l: " << l << " r: " << r << " c: " << c << endl;
        if (f[l] + f[r] <= X)
            ++c, ++l, --r;
        else
            --r, ++c;
    }

    return c + (l == r);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        vector<int> files;
        int disc;
        readTest(files, disc);
        cout << "Case #" << t << ": " << solve(files, disc) << endl;
    }
    return 0;
}
